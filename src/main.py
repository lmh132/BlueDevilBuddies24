#main script for matching, returns a csv of all pairings

from classes import Mentor, Mentee
from preprocess import cleanup, process_mentees, process_mentors

mentees = process_mentees(cleanup("src/testdata/menteeTest2.csv"))
mentors = process_mentors(cleanup("src/testdata/mentorTest2.csv"))

for mentee in mentees:
    print("Mentee: {}".format(mentee.fname + " " + mentee.lname))
    mentee.setPrefs(mentors)
    for i in range(len(mentee.preferences)):
        print("Mentor: {name} || {score}".format(name = mentee.preferences[i].fname + " " + mentee.preferences[i].lname, score = mentee.getCompatability(mentee.preferences[i])))
    print("----------------------")

for mentor in mentors:
    mentor.setPrefs(mentees)

pairings = {}

while len(mentees) > 0:
    mentee = mentees.pop(0)
    preferred_mentor = mentee.preferences.pop(0)
    if preferred_mentor not in pairings.keys():
        pairings[preferred_mentor] = mentee
    else:
        prev = pairings.pop(preferred_mentor)
        if preferred_mentor.preferences.index(mentee) < preferred_mentor.preferences.index(prev):
            pairings[preferred_mentor] = mentee
            mentees.append(prev)
        else:
            pairings[preferred_mentor] = prev
            mentees.append(mentee)

for mentor in pairings.keys():
    print("Mentor: {}".format(mentor.fname + " " + mentor.lname))
    print("Mentee: {}".format(pairings[mentor].fname + " " + pairings[mentor].lname))
    print("Compatability: {}".format(pairings[mentor].getCompatability(mentor)))
    print("----------------------")
