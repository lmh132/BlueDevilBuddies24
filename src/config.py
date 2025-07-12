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
# Questions are ordered to correspond between mentors and mentees at the same index

question_mapping = (("PB", Arch.CHOICES), # 1 Which country are you from?
                ("PB", Arch.CHOICES), # 2 Which state are you from?
                ("PB", Arch.SPECTRUM), # 3 Which best describes your hometown?
                ("AL", Arch.CHOICES), # 4 Are you in Trinity or Pratt?
                ("AL", Arch.MULTI), # 5 What is your intended major?
                ("AL", Arch.MULTI), # 6 Do you intend to complete any minors?
                ("AL", Arch.MULTI), # 7 Do you intend to complete any certificates?
                ("AL", Arch.SPECTRUM), # 8 How much academic advice are you willing to give?
                ("CL", Arch.CHOICES), # 9 What Quad do you feel the most connected to?
                ("CL", Arch.MULTI), # 10 What type of clubs are you a part of at Duke?
                ("CL", Arch.MULTI), # 11 What sports are you a part of at Duke?
                ("CL", Arch.MULTI), # 12 What affiliations do you identify with at Duke?
                ("AL", Arch.MULTI), # 13 What academic programs are/were you a part of at Duke?
                ("CL", Arch.CHOICES), # 14 What were you most looking forward to when coming to college?
                ("CL", Arch.CHOICES), # 15 What were you most nervous about coming into college?
                ("LS", Arch.SPECTRUM), # 16 Do you drink?
                ("LS", Arch.SPECTRUM), # 17 Do you use marijuana?
                ("LS", Arch.MULTI), # 18 How do you like to spend your free time?
                ("LS", Arch.SPECTRUM), # 19 How lively is your ideal Saturday night?
                ("LS", Arch.SPECTRUM), # 20 Which best reflects your use of social media?
                ("CL", Arch.SPECTRUM), # 21 How crazy are you about Duke Men's Basketball?
                ("GM", Arch.SPECTRUM), # 22 How often would you like to be in touch with your mentee over the summer?
                ("GM", Arch.SPECTRUM), # 23 How often would you like to be in touch with your mentee during the semester?
                ("GM", Arch.SPECTRUM), # 24 What kind of relationship are you looking for with your mentee?
                ("PB", Arch.CHOICES_NOMATCH), # 25 Which gender identity do you most identify with?
                ("PB", Arch.CHOICES_NOMATCH), # 26 Which ethnic/racial identity(s) do you most identify with?
                ("PB", Arch.CHOICES_NOMATCH), # 27 What sexual orientation do you most identify with?
                ("PB", Arch.CHOICES_NOMATCH), # 28 What is the current faith/religion you most closely follow?
                ("GM", Arch.YESNO), # 29 Will you be abroad this Fall (2025)?
                )

score_types = {
    "GM" : [Arch.SPECTRUM, Arch.SPECTRUM, Arch.SPECTRUM, Arch.YESNO, Arch.YESNO, Arch.YESNO],
    "AL" : [Arch.CHOICES, Arch.MULTI, Arch.MULTI, Arch.MULTI, Arch.SPECTRUM, Arch.MULTI],
    "CL" : [Arch.CHOICES, Arch.MULTI, Arch.MULTI, Arch.MULTI, Arch.CHOICES, Arch.CHOICES, Arch.SPECTRUM],
    "PB" : [Arch.CHOICES, Arch.CHOICES, Arch.SPECTRUM, Arch.CHOICES_NOMATCH, Arch.CHOICES_NOMATCH, Arch.CHOICES_NOMATCH, Arch.CHOICES_NOMATCH],
    "LS" : [Arch.SPECTRUM, Arch.SPECTRUM, Arch.MULTI, Arch.SPECTRUM, Arch.SPECTRUM]
}