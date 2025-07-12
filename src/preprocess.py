#This module is used to sift through Qualtrics csv data and return a list of mentor and mentee objects
#mentor and mentee forms have 33 corresponding questions, mentees have one extra question to determine weighting
#import question types and sections from config
#(For Mentees Only)Section Ranking

from classes import Mentor, Mentee
from config import question_mapping, Arch
from csv import *
import pandas as pd
from collections import defaultdict
import math
from pprint import pprint

def process_mentees(filename):
    df = pd.read_csv(filename)
    data = df.sort_values("Recorded Date").drop_duplicates(subset="NetID", keep="last")

    mentees = []

    for _, row in data.iterrows():
        responses = defaultdict(list)
        vals = row.values
        for i in range(29):
            raw = vals[i+1]  # +1 because itertuples includes index at row[0]
            match question_mapping[i][1]:
                case Arch.SPECTRUM:
                    try:
                        raw = int(raw)
                    except:
                        raw = 3
                case Arch.CHOICES:
                    raw = -1 if math.isnan(float(raw)) else int(raw)
                case Arch.MULTI:
                    raw = [-1] if type(raw) == float else [int(x) for x in raw.split(",")]
                case Arch.CHOICES_NOMATCH:
                    raw = 1 if math.isnan(float(raw)) else int(raw)
                    if raw == 1:
                        raw = -1
                case Arch.YESNO:
                    raw = 1 if type(raw) == float else int(raw)
            responses[question_mapping[i][0]].append(raw)

        match int(vals[34]):
            case 1:
                responses["GM"] += [0, 0]
            case 2:
                responses["GM"] += [0, 1]
            case 4:
                responses["GM"] += [1, 0]
        
        weights = {
            "GM" : 0.5,
            "AL" : 2.5,
            "CL" : 2,
            "PB" : 1.5,
            "LS" : 1,
        }

        if not pd.isna(vals[30]):
            weights["AL"] = 1 + (int(vals[30])-1)*0.5
            weights["CL"] = 1 + (int(vals[31])-1)*0.5
            weights["PB"] = 1 + (int(vals[32])-1)*0.5
            weights["LS"] = 1 + (int(vals[33])-1)*0.5

        phone = vals[35]
        netID = vals[36]
        fname = vals[37]
        lname = vals[38]
        email = vals[40]

        mentees.append(Mentee(fname, lname, netID, email, phone, responses, weights))
    
    return mentees

def process_mentors(filename):
    df = pd.read_csv(filename)
    data = df.sort_values("Recorded Date").drop_duplicates(subset="NetID", keep="last")

    mentors = []

    for idx, row in data.iterrows():
        responses = defaultdict(list)
        vals = row.values
        for i in range(29):
            raw = vals[i+1]  # +1 because itertuples includes index at row[0]
            match question_mapping[i][1]:
                case Arch.SPECTRUM:
                    try:
                        raw = int(raw)
                    except:
                        raw = 3
                case Arch.CHOICES:
                    raw = -1 if math.isnan(float(raw)) else int(raw)
                case Arch.MULTI:
                    raw = [-1] if type(raw) == float else [int(x) for x in raw.split(",")]
                case Arch.CHOICES_NOMATCH:
                    raw = 1 if math.isnan(float(raw)) else int(raw)
                    if raw == 1:
                        raw = -1
                case Arch.YESNO:
                    raw = 1 if type(raw) == float else int(raw)
            responses[question_mapping[i][0]].append(raw)
    
        if int(vals[30]) == 1:
            responses["GM"].append(0)
        else:
            responses["GM"].append(1)
        
        if int(vals[31]) == 1:
            responses["GM"].append(1)
        else:
            responses["GM"].append(0)

        phone = vals[32]
        netID = vals[33]
        fname = vals[34]
        lname = vals[35]
        email = vals[37]

        mentors.append(Mentor(fname, lname, netID, email, phone, responses))

    return mentors

process_mentees("25/mentees-25.csv")