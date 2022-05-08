"""Maori Quiz Questions/Randomizer v3
Formats text a bit
                                turns into a function?
"""

player = 0
TOTAL = 10

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

QUESTION_1 = "one"  # the first questions
QUESTION_2 = "two"  # the second question
QUESTION_3 = "three"  # etc...
QUESTION_4 = "four"
QUESTION_5 = "five"
QUESTION_6 = "six"
QUESTION_7 = "seven"
QUESTION_8 = "eight"
QUESTION_9 = "nine"
QUESTION_10 = "ten"

ANSWER_1 = "tahi"  # the first answer
ANSWER_2 = "rua"  # the second answer
ANSWER_3 = "toru"  # etc...
ANSWER_4 = "wha"
ANSWER_5 = "rima"
ANSWER_6 = "ono"
ANSWER_7 = "whitu"
ANSWER_8 = "waru"
ANSWER_9 = "iwa"
ANSWER_10 = "tekau"


def questions():
    ask_1 = input(f"What is the maori version of {QUESTION_1}? (No Macron's): ")  # asks the user a question
    if ask_1 == ANSWER_1:  # if they get it right display total and congratulations message
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:  # if they get it wrong display the correct answer and total
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was {ANSWER_1}")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_2 = input(f"What is the maori version of {QUESTION_2}? (No Macron's): ")
    if ask_2 == ANSWER_2:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was {ANSWER_2}")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_3 = input(f"What is the maori version of {QUESTION_3}? (No Macron's): ")
    if ask_3 == ANSWER_3:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was {ANSWER_3}")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_4 = input(f"What is the maori version of {QUESTION_4}? (No Macron's): ")
    if ask_4 == ANSWER_4:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was {ANSWER_4}")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_5 = input(f"What is the maori version of {QUESTION_5}? (No Macron's): ")
    if ask_5 == ANSWER_5:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was {ANSWER_5}")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_6 = input(f"What is the maori version of {QUESTION_6}? (No Macron's): ")
    if ask_6 == ANSWER_6:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was {ANSWER_6}")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_7 = input(f"What is the maori version of {QUESTION_7}? (No Macron's): ")
    if ask_7 == ANSWER_7:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was {ANSWER_7}")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_8 = input(f"What is the maori version of {QUESTION_8}? (No Macron's): ")
    if ask_8 == ANSWER_8:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was {ANSWER_8}")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_9 = input(f"What is the maori version of {QUESTION_9}? (No Macron's): ")
    if ask_9 == ANSWER_9:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was {ANSWER_9}")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_10 = input(f"What is the maori version of {QUESTION_10}? (No Macron's): ")
    if ask_10 == ANSWER_10:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was {ANSWER_10}")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()


# Main Routine...
