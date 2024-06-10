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
question_dict = {
    "Q1" : Arch.SPECTRUM, 
    "Q2" : Arch.SPECTRUM, 
    "Q3" : Arch.SPECTRUM, 
    "Q4" : Arch.YESNO, 
    "Q5" : Arch.MULTI, 
    "Q6" : Arch.MULTI, 
    "Q7" : Arch.MULTI, 
    "Q8" : Arch.CHOICES, 
    "Q9" : Arch.SPECTRUM, 
    "Q10" : Arch.CHOICES, 
    "Q11" : Arch.CHOICES, 
    "Q12" : Arch.CHOICES, 
    "Q13" : Arch.CHOICES, 
    "Q14" : Arch.CHOICES, 
    "Q15" : Arch.MULTI, 
    "Q16" : Arch.SPECTRUM, 
    "Q17" : Arch.CHOICES, 
    "Q18" : Arch.CHOICES, 
    "Q19" : Arch.SPECTRUM, 
    "Q20" : Arch.CHOICES_NOMATCH, 
    "Q21" : Arch.CHOICES_NOMATCH, 
    "Q22" : Arch.CHOICES_NOMATCH, 
    "Q23" : Arch.CHOICES, 
    "Q24" : Arch.CHOICES, 
    "Q25" : Arch.CHOICES_NOMATCH, 
    "Q26" : Arch.SPECTRUM, 
    "Q27" : Arch.SPECTRUM, 
    "Q28" : Arch.MULTI, 
    "Q29" : Arch.SPECTRUM, 
    "Q30" : Arch.SPECTRUM, 
}
