#main script for matching, returns a csv of all pairings

from classes import Mentor, Mentee, calc_compatability
from preprocess import process_mentees, process_mentors
import pandas as pd
import pickle

mentees = process_mentees(pd.read_csv("data/real/'24/mentees.csv"))
mentors = process_mentors(pd.read_csv("data/real/'24/mentors.csv"))
for mentee in mentees:
    mentee.pairing_ranking = sorted(mentors, key = lambda x: calc_compatability(mentee, x), reverse=True)

for mentor in mentors:
    #mentor.to_string()
    mentor.pairing_ranking = sorted(mentees, key = lambda x: calc_compatability(x, mentor), reverse=True)
"""
mentees[0].to_string()
print("--------------------")
for m in mentees[0].pairing_ranking[:5]:
    m.to_string()
    calc_compatability(mentees[0], m, verbose = True)
"""

pairings = {}

while len(mentees) > 0:
    mentee = mentees.pop(0)
    preferred_mentor = mentee.pairing_ranking.pop(0)
    if preferred_mentor not in pairings.keys():
        pairings[preferred_mentor] = mentee
    else:
        prev = pairings.pop(preferred_mentor)
        if preferred_mentor.pairing_ranking.index(mentee) < preferred_mentor.pairing_ranking.index(prev):
            pairings[preferred_mentor] = mentee
            mentees.append(prev)
        else:
            pairings[preferred_mentor] = prev
            mentees.append(mentee)
"""
for mentor in pairings.keys():
    print("Mentor: {}".format(mentor.fname + " " + mentor.lname))
    print("Mentee: {}".format(pairings[mentor].fname + " " + pairings[mentor].lname))
    print("Compatability: {}".format(calc_compatability(pairings[mentor], mentor)))
    print("----------------------")
"""

f = open("data/real/'24/pairings.pkl", "wb")
pickle.dump(pairings, f)
f.close()

nomatch = [x for x in mentors if x not in pairings.keys()]
f = open("data/real/'24/leftovers.pkl", "wb")
pickle.dump(nomatch, f)
f.close()