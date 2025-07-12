import pickle
import csv

with open("25/pairings-25.pkl", "rb") as pkl:
    with open("25/pairings-25.csv", "w") as f:
        pairings = pickle.load(pkl)
        writer = csv.writer(f)

        writer.writerow(["Mentor", "Mentor netID", "Mentor email", "Mentee", "Mentee netID", "Mentee email", "Compatability Score"])
        for pairing in pairings.items():
            mentor = pairing[0]
            mentee = pairing[1]
            writer.writerow(["{f} {l}".format(f = mentor.fname, l = mentor.lname), mentor.netID, mentor.email, "{f} {l}".format(f = mentee.fname, l = mentee.lname), mentee.netID, mentee.email])

        f.close()
    pkl.close()

with open("25/leftovers.pkl", "rb") as pkl:
    with open("25/leftovers.csv", "w") as f:
        leftovers = pickle.load(pkl)
        writer = csv.writer(f)

        writer.writerow(["Mentor", "Mentor netID", "Mentor email"])
        for mentor in leftovers:
            writer.writerow(["{f} {l}".format(f = mentor.fname, l = mentor.lname), mentor.netID, mentor.email])

        f.close()
    pkl.close()

