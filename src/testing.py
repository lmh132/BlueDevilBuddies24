import pickle
import pprint
from classes import Mentee, Mentor
def print_leftovers():
    f = open("data/real/'24/leftovers.pkl", "rb")
    leftovers = pickle.load(f)
    for i, mentor in enumerate(leftovers):
        print(i)
        mentor.to_string()

def match_search():
    f = open("data/real/'24/pairings.pkl", "rb")
    pairings = pickle.load(f)
    name = ""
    while name != "STOP":
        for mentor in pairings.keys():
            print(mentor.netID)
            if mentor.netID == name:
                pairings[mentor].to_string()
        name = input("Search for: ")
    f.close()

match_search()