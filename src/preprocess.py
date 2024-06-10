#This module is used to sift through Qualtrics csv data and return a list of mentor and mentee objects
#mentor and mentee forms have 33 corresponding questions, mentees have one extra question to determine weighting
#import question types and sections from config
#(For Mentees Only)Section Ranking

from classes import Mentor, Mentee
from config import Arch, question_dict
from csv import *
import pandas as pd


def cleanup(filename: str):
    data = pd.read_csv(filename)
    data = data.drop([0, 1], axis = 0) #dropping inital rows of metadata

    data = data.drop(["StartDate", "EndDate", "Status", "IPAddress", "Progress", "Duration (in seconds)", 
                      "Finished", "RecordedDate", "ResponseId", "ExternalReference", "LocationLatitude", 
                      "LocationLongitude", "DistributionChannel", "UserLanguage", "N/A_Browser", "N/A_Version", 
                      "N/A_Operating System", "N/A_Resolution", "RecipientLastName", 
                      "RecipientFirstName", "RecipientEmail"], axis = 1) #dropping unneeded columns
    
    return data

def process_mentees(data: pd.DataFrame) -> list[Mentee]:
    ret = [] #list of mentees to return
    for row in data.itertuples():
        scores = [] #array to hold all score values
        for i in range(1, len(question_dict)+1):
            val = row[i]
            if question_dict["Q{n}".format(n = i)] == Arch.MULTI:
                val = [int(x) for x in val.split(",")]
            else:
                val = int(val) if type(val) == str else -1 #for some reason the blanks are read in as floats?

            scores.append(val)
        rankings = {
            "GM" : 5,
            "CL" : 5-int(row[31]),
            "AL" : 5-int(row[32]),
            "PB" : 5-int(row[33]),
            "LS" : 5-int(row[34])
        }
        NetID = row[35]
        fname = row[36]
        lname = row[37]
        email = row[40]
        mentee = Mentee(fname, lname, NetID, email, rankings) #creating new mentee object
        mentee.setSectionArrays(scores)
        ret.append(mentee)

    return ret

    

def process_mentors(data: pd.DataFrame) -> list[Mentor]:
    ret = [] #list of mentees to return
    for row in data.itertuples():
        scores = [] #array to hold all score values
        for i in range(1, len(question_dict)+1):
            val = row[i]
            if question_dict["Q{n}".format(n = i)] == Arch.MULTI:
                val = [int(x) for x in val.split(",")]
            else:
                val = int(val) if type(val) == str else -1 #for some reason the blanks are read in as floats?

            scores.append(val)
        NetID = row[31]
        fname = row[32]
        lname = row[33]
        email = row[36]
        mentor = Mentor(fname, lname, NetID, email) #creating new mentee object
        mentor.setSectionArrays(scores)
        ret.append(mentor)

    return ret


