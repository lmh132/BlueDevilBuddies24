import pickle
import csv

with open("data/real/'24/pairings.pkl", "rb") as pkl:
    with open("data/real/'24/pairings.csv", "w") as f:
        pairings = pickle.load(pkl)
        writer = csv.writer(f)

        writer.writerow(["Mentor", "Mentor netID", "Mentor email", "Mentee", "Mentee netID", "Mentee email"])
        for pairing in pairings.items():
            mentor = pairing[0]
            mentee = pairing[1]
            writer.writerow(["{f} {l}".format(f = mentor.fname, l = mentor.lname), mentor.netID, mentor.email, "{f} {l}".format(f = mentee.fname, l = mentee.lname), mentee.netID, mentee.email])

        f.close()
    pkl.close()

with open("data/real/'24/leftovers.pkl", "rb") as pkl:
    with open("data/real/'24/leftovers.csv", "w") as f:
        leftovers = pickle.load(pkl)
        writer = csv.writer(f)

        writer.writerow(["Mentor", "Mentor netID", "Mentor email"])
        for mentor in leftovers:
            writer.writerow(["{f} {l}".format(f = mentor.fname, l = mentor.lname), mentor.netID, mentor.email])

        f.close()
    pkl.close()

