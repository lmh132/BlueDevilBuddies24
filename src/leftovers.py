import pandas as pd
from classes import Mentee, Mentor
import pickle
import csv

f = open("data/real/'24/pairings.pkl", "rb")
pairs = pickle.load(f)
f.close()

matched_mentors = [mentor.netID for mentor in pairs.keys()]
matched_mentees = [mentee.netID for mentee in pairs.values()]

drop = []

mentors_df = pd.read_csv("data/real/'24/mentor_words.csv")
for index, row in mentors_df.iterrows():
    if row.iloc[59] in matched_mentors:
        #print("dropped {}".format(row.iloc[59]))
        drop.append(index)

mentors_df = mentors_df.drop([0, 1], axis = 0) #dropping inital rows of metadata
mentors_df = mentors_df.drop(["StartDate", "EndDate", "Status", "IPAddress", "Progress", "Duration (in seconds)", 
                    "Finished", "RecordedDate", "ResponseId", "ExternalReference", "LocationLatitude", 
                    "LocationLongitude", "DistributionChannel", "UserLanguage", "Q1_Browser", "Q1_Version", 
                    "Q1_Operating System", "Q1_Resolution", "RecipientLastName", 
                    "RecipientFirstName", "RecipientEmail"], axis = 1)
mentors_df = mentors_df.drop(drop, axis = 0)
mentors_df.to_csv("results/leftover_mentors.csv")

drop.clear()

mentees_df = pd.read_csv("data/real/'24/mentee_words.csv")
for index, row in mentees_df.iterrows():
    if row.iloc[60] in matched_mentees:
        #print("dropped {}".format(row.iloc[60]))
        drop.append(index)

mentees_df = mentees_df.drop(drop, axis = 0)


mentees_df = mentees_df.drop([0, 1], axis = 0) #dropping inital rows of metadata
mentees_df = mentees_df.drop(["StartDate", "EndDate", "Status", "IPAddress", "Progress", "Duration (in seconds)", 
                    "Finished", "RecordedDate", "ResponseId", "ExternalReference", "LocationLatitude", 
                    "LocationLongitude", "DistributionChannel", "UserLanguage", "Q1_Browser", "Q1_Version", 
                    "Q1_Operating System", "Q1_Resolution", "RecipientLastName", 
                    "RecipientFirstName", "RecipientEmail"], axis = 1)
mentees_df.to_csv("results/leftover_mentees.csv")