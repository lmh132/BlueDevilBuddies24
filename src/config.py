from enum import Enum

#defining question archetypes
class Arch(Enum):
    SPECTRUM = 1 #multiplier for spectrum type questions
    CHOICES = 2 #multiplier for select one multiple choice
    CHOICES_NOMATCH = 3 #multiplier for multiple choice questions the user can choose to not use as a pairing factor
    MULTI = 4 #multiplier for select one or more multiple choice
    YESNO = 5#multiplier for yes/no questions

#listing out which questions correspond to which sections
#GM == General Mentorship
#CL == Campus Life
#AL == Academic Life
#PB == Personal Background
#LS == Lifestyle
#Format: Question# : (Section, Question Type)
mentors_dict = (("PB", Arch.CHOICES),
                ("PB", Arch.CHOICES),
                ("PB", Arch.SPECTRUM),
                ("GM", Arch.YESNO),
                ("GM", Arch.YESNO),
                ("CL", Arch.CHOICES),
                ("AL", Arch.CHOICES),
                ("AL", Arch.MULTI),
                ("AL", Arch.MULTI),
                ("AL", Arch.MULTI),
                ("AL", Arch.SPECTRUM),
                ("CL", Arch.MULTI),
                ("CL", Arch.MULTI),
                ("CL", Arch.MULTI),
                ("AL", Arch.MULTI),
                ("CL", Arch.CHOICES),
                ("CL", Arch.CHOICES),
                ("LS", Arch.SPECTRUM),
                ("LS", Arch.SPECTRUM),
                ("LS", Arch.MULTI),
                ("LS", Arch.SPECTRUM),
                ("LS", Arch.SPECTRUM),
                ("CL", Arch.SPECTRUM),
                ("GM", Arch.SPECTRUM),
                ("GM", Arch.SPECTRUM),
                ("GM", Arch.SPECTRUM),
                ("PB", Arch.CHOICES_NOMATCH),
                ("PB", Arch.CHOICES_NOMATCH),
                ("PB", Arch.CHOICES_NOMATCH),
                ("PB", Arch.CHOICES_NOMATCH),
                ("GM", Arch.YESNO),
                ("GM", Arch.YESNO))

mentees_dict = (("GM", Arch.CHOICES),
                ("PB", Arch.CHOICES),
                ("PB", Arch.CHOICES),
                ("PB", Arch.SPECTRUM),
                ("AL", Arch.CHOICES),
                ("AL", Arch.MULTI),
                ("AL", Arch.MULTI),
                ("AL", Arch.MULTI),
                ("AL", Arch.SPECTRUM),
                ("CL", Arch.CHOICES),
                ("CL", Arch.MULTI),
                ("CL", Arch.MULTI),
                ("CL", Arch.MULTI),
                ("AL", Arch.MULTI),
                ("CL", Arch.CHOICES),
                ("CL", Arch.CHOICES),
                ("LS", Arch.SPECTRUM),
                ("LS", Arch.SPECTRUM),
                ("LS", Arch.MULTI),
                ("LS", Arch.SPECTRUM),
                ("LS", Arch.SPECTRUM),
                ("CL", Arch.SPECTRUM),
                ("GM", Arch.SPECTRUM),
                ("GM", Arch.SPECTRUM),
                ("GM", Arch.SPECTRUM),
                ("PB", Arch.CHOICES_NOMATCH),
                ("PB", Arch.CHOICES_NOMATCH),
                ("PB", Arch.CHOICES_NOMATCH),
                ("PB", Arch.CHOICES_NOMATCH),
                ("GM", Arch.YESNO))

score_types = {
    "GM" : [Arch.YESNO, Arch.YESNO, Arch.SPECTRUM, Arch.SPECTRUM, Arch.SPECTRUM, Arch.YESNO],
    "AL" : [Arch.CHOICES, Arch.MULTI, Arch.MULTI, Arch.MULTI, Arch.SPECTRUM, Arch.MULTI],
    "CL" : [Arch.CHOICES, Arch.MULTI, Arch.MULTI, Arch.MULTI, Arch.CHOICES, Arch.CHOICES, Arch.SPECTRUM],
    "PB" : [Arch.CHOICES, Arch.CHOICES, Arch.SPECTRUM, Arch.CHOICES_NOMATCH, Arch.CHOICES_NOMATCH, Arch.CHOICES_NOMATCH, Arch.CHOICES_NOMATCH],
    "LS" : [Arch.SPECTRUM, Arch.SPECTRUM, Arch.MULTI, Arch.SPECTRUM, Arch.SPECTRUM]
}