"""Maori Quiz Questions/Randomizer v2
Splits the list from 05_questions_randomizer_v1 into 2 lists
with questions and answers separated into different variables
"""

import random

QUESTIONS_ENGLISH = ["one", "two", "three",
                     "four", "five", "six",
                     "seven", "eight", "nine",
                     "ten"]  # A list storing all the data for the english questions

ANSWERS_MAORI = ["tahi", "rua", "toru",
                 "wha", "rima", "ono",
                 "whitu", "waru", "iwa",
                 "tekau"]  # A list storing all the answers for the questions

random = random.randint(0, 9)  # imports a random number

ask_1 = ""  # provides the variables for users to
ask_2 = ""  # input their answers into
ask_3 = ""
ask_4 = ""
ask_5 = ""
ask_6 = ""
ask_7 = ""
ask_8 = ""
ask_9 = ""
ask_10 = ""

question_1 = QUESTIONS_ENGLISH[0]  # the first questions
question_2 = QUESTIONS_ENGLISH[1]  # the second question
question_3 = QUESTIONS_ENGLISH[2]  # etc...
question_4 = QUESTIONS_ENGLISH[3]
question_5 = QUESTIONS_ENGLISH[4]
question_6 = QUESTIONS_ENGLISH[5]
question_7 = QUESTIONS_ENGLISH[6]
question_8 = QUESTIONS_ENGLISH[7]
question_9 = QUESTIONS_ENGLISH[8]
question_10 = QUESTIONS_ENGLISH[9]

answer_1 = ANSWERS_MAORI[0]
answer_2 = ANSWERS_MAORI[1]
answer_3 = ANSWERS_MAORI[2]
answer_4 = ANSWERS_MAORI[3]
answer_5 = ANSWERS_MAORI[4]
answer_6 = ANSWERS_MAORI[5]
answer_7 = ANSWERS_MAORI[6]
answer_8 = ANSWERS_MAORI[7]
answer_9 = ANSWERS_MAORI[8]
answer_10 = ANSWERS_MAORI[9]

# Main Routine...
ask_1 = input(f"What is the maori version of {question_1}?: ")
