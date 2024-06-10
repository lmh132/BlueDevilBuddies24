#this module holds the constructors for the mentor and mentee classes used in other scripts
from config import Arch, question_dict
from statistics import mean

class Person:
    def __init__(self, fname, lname, netID, email):
        self.fname = fname
        self.lname = lname
        self.netID = netID
        self.email = email
        self.scoreArray = []

    def setSectionArrays(self, scores):
        self.scoreArray = scores

class Mentee(Person):
    def __init__(self, fname, lname, netID, email, sectionRankings):
        super().__init__(fname, lname, netID, email)
        self.sectionRankings = sectionRankings
        

    def getCompatability(self, mentor: Person):
        #general_mentorship = self.scoreArray[0:4]
        weightedScores = []
        for i in range(len(self.scoreArray)):
            raw = 0
            match question_dict["Q{n}".format(n = i+1)]:
                case Arch.SPECTRUM:
                    raw = 4-(abs(self.scoreArray[i]-mentor.scoreArray[i]))
                case Arch.CHOICES:
                    raw = 4 if self.scoreArray[i] == mentor.scoreArray[i] else 0
                case Arch.CHOICES_NOMATCH:
                    raw = 4 if self.scoreArray[i] == mentor.scoreArray[i] else None
                case Arch.MULTI:
                    for choice in self.scoreArray[i]:
                        if choice in mentor.scoreArray[i]:
                            raw+=1
                case Arch.YESNO:
                    raw = 4 if self.scoreArray[i] == mentor.scoreArray[i] else 0
            weightedScores.append(raw)
        gm_score = mean([x for x in weightedScores[0:4] if x != None]) * self.sectionRankings["GM"]
        cl_score = mean([x for x in weightedScores[4:10] if x != None]) * self.sectionRankings["CL"]
        al_score = mean([x for x in weightedScores[10:16] if x != None]) * self.sectionRankings["AL"]
        pb_score = mean([x for x in weightedScores[16:26] if x != None]) * self.sectionRankings["PB"]
        ls_score = mean([x for x in weightedScores[26:31] if x != None]) * self.sectionRankings["LS"]

        return gm_score+cl_score+al_score+pb_score+ls_score
    
    def setPrefs(self, mentors):
        self.preferences = sorted(mentors, key = lambda x: self.getCompatability(x), reverse = True)


class Mentor(Person):
    def __init__(self, fname, lname, netID, email):
        super().__init__(fname, lname, netID, email)
        self.preferences = []

    def setPrefs(self, mentees):
        self.preferences = sorted(mentees, key = lambda x: x.getCompatability(self), reverse = True)