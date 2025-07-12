#main script for matching, returns a csv of all pairings

from classes import Mentor, Mentee, calc_compatability
from preprocess import process_mentees, process_mentors
import pandas as pd
import pickle

mentees = process_mentees("25/mentees-25.csv")
mentors = process_mentors("25/mentors-25.csv")
for mentee in mentees:
    mentee.pairing_ranking = sorted(mentors, key = lambda x: calc_compatability(mentee, x), reverse=True)

for mentor in mentors:
    mentor.pairing_ranking = sorted(mentees, key = lambda x: calc_compatability(x, mentor), reverse=True)

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

print("Pairings complete, {} mentees matched".format(len(pairings)))
for mentor in pairings.keys():
    mentor_netID = mentor.netID
    mentee_netID = pairings[mentor].netID
    score = calc_compatability(pairings[mentor], mentor)
    

f = open("25/pairings-25.pkl", "wb")
pickle.dump(pairings, f)
f.close()

nomatch = [x for x in mentors if x not in pairings.keys()]
f = open("25/leftovers.pkl", "wb")
pickle.dump(nomatch, f)
f.close()
