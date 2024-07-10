#This module is used to sift through Qualtrics csv data and return a list of mentor and mentee objects
#mentor and mentee forms have 33 corresponding questions, mentees have one extra question to determine weighting
#import question types and sections from config
#(For Mentees Only)Section Ranking

from classes import Mentor, Mentee
from config import mentors_dict, mentees_dict, Arch
from csv import *
import pandas as pd
from collections import defaultdict
import math


def cleanup(filename: str):
    data = pd.read_csv(filename)
    data = data.drop([0, 1], axis = 0) #dropping inital rows of metadata

    data = data.drop(["StartDate", "EndDate", "Status", "IPAddress", "Progress", "Duration (in seconds)", 
                      "Finished", "RecordedDate", "ResponseId", "ExternalReference", "LocationLatitude", 
                      "LocationLongitude", "DistributionChannel", "UserLanguage", "Q1_Browser", "Q1_Version", 
                      "Q1_Operating System", "Q1_Resolution", "RecipientLastName", 
                      "RecipientFirstName", "RecipientEmail", "Q5", "Q7", "Q34", "Q35"], axis = 1) #dropping unneeded columns
    
    return data

def process_mentees(data: pd.DataFrame) -> list[Mentee]:
    ret = [] #list of mentees to return
    for row in data.itertuples():
        scores = defaultdict(list)
        
        for i in range(2, len(mentees_dict)+2):
            raw = row[i]
            #print(type(raw), raw, mentees_dict[i-2])
            match mentees_dict[i-2][1]:
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
            scores[mentees_dict[i-2][0]].append(raw)
        weights = {
            "GM" : 1.5,
            "AL" : 2,
            "CL" : 1.5,
            "PB" : 1,
            "LS" : 0.5,
        }
        if type(row[33]) != float:
            weights["AL"] = int(row[33])
            weights["CL"] = int(row[33])
            weights["PBL"] = int(row[33])
            weights["LS"] = int(row[33])
        
        number = str(row[36]).replace(" ", "").replace("-", "")
        netID = str(row[37])
        first, last = str(row[38]), str(row[39])
        email = str(row[41])

        mentee = Mentee(fname=first, lname=last, netID=netID, email=email, number=number, responses=scores, weights=weights)
        mentee.set_arr()
        #mentee.to_string()
        ret.append(mentee)

    print("{l} mentees processed".format(l = len(ret)))
    return ret

def process_mentors(data: pd.DataFrame) -> list[Mentor]:
    ret = [] #list of mentors to return
    for row in data.itertuples():
        scores = defaultdict(list)
        for i in range(2, len(mentors_dict)+2):
            raw = row[i]
            match mentors_dict[i-2][1]:
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
            scores[mentors_dict[i-2][0]].append(raw)
        
        number = str(row[34]).replace(" ", "").replace("-", "")
        netID = str(row[35])
        first, last = str(row[36]), str(row[37])
        email = str(row[39])

        mentor = Mentor(fname=first, lname=last, netID=netID, email=email, number=number, responses=scores)
        mentor.set_arr()
        #mentor.to_string()
        ret.append(mentor)

    print("{l} mentors processed".format(l = len(ret)))
    return ret