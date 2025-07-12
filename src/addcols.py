import csv
import pandas as pd

file = "data/real/'24/pairings_final.csv"

pairings = pd.read_csv(file)
mentee_info = pd.read_csv("data/real/'24/mentee_words_updated.csv")
mentor_info = pd.read_csv("data/real/'24/mentor_words.csv")

with open("results/final.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Mentor Name", "Mentor netID", "Mentor Email", "Mentor School", "Mentor Major(s)", "Mentor Minor(s)", "Mentor Certificate(s)", "Mentor Program(s)", "Mentor Hobbie(s)",
                     "Mentee Name", "Mentee netID", "Mentee Email", "Mentee School", "Mentee Major(s)", "Mentee Minor(s)", "Mentee Certificate(s)", "Mentee Program(s)", "Mentee Hobbie(s)"])
    for row in pairings.itertuples():
        mentor_id = row[2]
        mentee_id = row[5]
        mentor_row, mentee_row = [], []

        #print(mentor_id, mentee_id)

        for mentor in mentor_info.itertuples():
            #print(mentor[60])
            if mentor[60] == mentor_id:
                mentor_row = ["{f} {l}".format(f = mentor[61], l = mentor[62]), mentor[60], mentor[64], mentor[30], mentor[31], mentor[32], mentor[33], mentor[38], mentor[43]]
                #print(mentor_row)
                break
        for mentee in mentee_info.itertuples():
            #print(mentee[61])
            if mentee[61] == mentee_id:
                #print(mentee[42])
                mentee_row = ["{f} {l}".format(f = mentee[62], l = mentee[63]), mentee[61], mentee[65], mentee[27], mentee[28], mentee[29], mentee[30], mentee[37], mentee[42]]
                #print(mentee_row)
                break
        if not mentor_row:
            print(mentor_id, "Not found")
        if not mentee_row:
            print(mentee_id, "Not found")
            
        writer.writerow(mentor_row+mentee_row)

    f.close()