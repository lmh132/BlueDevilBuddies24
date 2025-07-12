#this module holds the constructors for the mentor and mentee classes used in other scripts
from config import Arch
from statistics import mean
from pprint import pprint
from config import score_types

class Person:
    def __init__(self, fname, lname, netID, email, number, responses):
        self.fname = fname
        self.lname = lname
        self.netID = netID
        self.email = email
        self.number = number
        self.responses = responses
        self.pairing_ranking = []

    def to_string(self):
        return "{f} {l} || {n} || {p} || {e}".format(f = self.fname, l = self.lname, n = self.netID, p = self.number, e = self.email)
        #print(self.responses)

class Mentee(Person):
    def __init__(self, fname, lname, netID, email, number, responses, weights):
        super().__init__(fname, lname, netID, email, number, responses)
        self.weights = weights
        self.set_quad()

    def set_quad(self):
        match self.responses["CL"][0]:
            case 2 | 10: #pegram or basset -> craven
                self.responses["CL"][0] = 1
            case 9 | 16:
                self.responses["CL"][0] = 2
            case 3 | 13:
                self.responses["CL"][0] = 3
            case 7 | 12:
                self.responses["CL"][0] = 5
            case 4 | 11 :
                self.responses["CL"][0] = 6
            case 1 | 5:
                self.responses["CL"][0] = 7
            case 14:
                self.responses["CL"][0] = 9
            case 17:
                self.responses["CL"][0] = 11

    def to_string(self):
        return super().to_string()+"GM: {gm} | AL: {al} | CL: {cl} | PB: {pb} | LS: {ls}".format(gm=self.weights["GM"], al=self.weights["AL"], cl=self.weights["CL"], pb=self.weights["PB"], ls = self.weights["LS"])

class Mentor(Person):
    def __init__(self, fname, lname, netID, email, number, responses):
        super().__init__(fname, lname, netID, email, number, responses)

    def set_arr(self):
        mentor_arr = [0]*6
        if self.responses["GM"][0] == 2: #transfer
            mentor_arr[1] = 1
        if self.responses["GM"][1] == 1: #gap year
            mentor_arr[0] = 1

        for i in range(2, 5): #spectrum questions x3
            mentor_arr[i] = self.responses["GM"][i]

        if self.responses["GM"][5] == 2: #willing to mentor transfer
            mentor_arr[1] = 0
        
        if self.responses["GM"][6] == 2:
            mentor_arr[5] = 1
        
        self.responses["GM"] = mentor_arr

def calc_compatability(mentee: Mentee, mentor: Mentor, verbose = False):
    total = 0
    for section in ["GM", "AL", "CL", "PB", "LS"]:
        score = 0
        x = mentee.responses[section]
        y = mentor.responses[section]
        maximum = len(score_types[section])*4
        for i in range(len(x)):
            if verbose: print(x[i], y[i], score_types[section][i])
            match score_types[section][i]:
                case Arch.SPECTRUM:
                    score += 4-abs(x[i] - y[i])
                case Arch.CHOICES:
                    if section == "AL" and i == 0:
                        if x[i] != y[i]:
                            score -= 100000
                    if x[i] == y[i]:
                        score += 4
                case Arch.MULTI:
                    for thing in x[i]:
                        if thing in y[i]:
                            score += 2
                case Arch.CHOICES_NOMATCH:
                    if x[i] != -1 and y[i] != -1:
                        if x[i] == y[i]:
                            score += 6
                    else:
                        maximum -= 4
                case Arch.YESNO:
                    if x[i] == y[i]:
                        score += 4
        score = score/maximum
        if verbose: print("-----{s} Compatability: {n}-----".format(s = section, n = score))
        total += score * mentee.weights[section]
    if verbose: print("-----Overall Compatability: {n}-----".format(n = total))
    return total
