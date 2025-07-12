import pickle
import pprint
from classes import calc_compatability
def print_leftovers():
    f = open("data/real/'24/leftovers.pkl", "rb")
    leftovers = pickle.load(f)
    for mentor in leftovers:
        mentor.to_string()

def match_search():
    f = open("25/pairings-25.pkl", "rb")
    pairings = pickle.load(f)
    name = ""
    while name != "STOP":
        for mentor in pairings.keys():
            if mentor.netID == name:
                print(pairings[mentor].to_string())
                print(calc_compatability(pairings[mentor], mentor, True))
        print("=============================================")
        name = input("Search for: ")
    f.close()

def get_stats():
    f = open("25/pairings-25.pkl", "rb")
    pairings = pickle.load(f)

    scores = []

    for mentor, mentee in pairings.items():
        scores.append((calc_compatability(mentee, mentor), mentor, mentee))

    scores.sort(key = lambda x: x[0])

    print("Highest compatability: {}".format(scores[-1][0]))
    print("Mentor: {}".format(scores[-1][1].to_string()))
    print("Mentee: {}".format(scores[-1][2].to_string()))
    print("=============================================")
    print("Lowest compatability: {}".format(scores[0][0]))
    print("Mentor: {}".format(scores[0][1].to_string()))
    print("Mentee: {}".format(scores[0][2].to_string()))

get_stats()
match_search()