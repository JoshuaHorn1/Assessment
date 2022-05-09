"""Maori Quiz (Numbers 1-10) Base code v2
Components added after testing/trialling
"""

# Functions go here...


# Yes/No checking function:
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes, output 'program continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # if they say no, output 'display instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # otherwise - show error
        else:
            print("Please answer 'Yes (Y)' or 'No (N)'")


# Function used to display instructions:
def display_instructions():
    print("**** How to Play ****\n"
          "\n"
          "(how to use the program will go here)\n"
          "\n")


# function containing questions and data
def questions():

    player = 0

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

    question_1 = "one"  # the first questions
    question_2 = "two"  # the second question
    question_3 = "three"  # etc...
    question_4 = "four"
    question_5 = "five"
    question_6 = "six"
    question_7 = "seven"
    question_8 = "eight"
    question_9 = "nine"
    question_10 = "ten"

    answer_1 = "tahi"  # the first answer
    answer_2 = "rua"  # the second answer
    answer_3 = "toru"  # etc...
    answer_4 = "wha"
    answer_5 = "rima"
    answer_6 = "ono"
    answer_7 = "whitu"
    answer_8 = "waru"
    answer_9 = "iwa"
    answer_10 = "tekau"

    ask_1 = input(f"What is the maori version of '{QUESTION_1}'? (No Macron's): ")  # asks the user a question
    if ask_1 == ANSWER_1:  # if they get it right display total and congratulations message
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:  # if they get it wrong display the correct answer and total
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{ANSWER_1}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_2 = input(f"What is the maori version of '{QUESTION_2}'? (No Macron's): ")
    if ask_2 == ANSWER_2:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{ANSWER_2}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_3 = input(f"What is the maori version of '{QUESTION_3}'? (No Macron's): ")
    if ask_3 == ANSWER_3:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{ANSWER_3}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_4 = input(f"What is the maori version of '{QUESTION_4}'? (No Macron's): ")
    if ask_4 == ANSWER_4:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{ANSWER_4}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_5 = input(f"What is the maori version of '{QUESTION_5}'? (No Macron's): ")
    if ask_5 == ANSWER_5:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{ANSWER_5}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_6 = input(f"What is the maori version of '{QUESTION_6}'? (No Macron's): ")
    if ask_6 == ANSWER_6:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{ANSWER_6}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_7 = input(f"What is the maori version of '{QUESTION_7}'? (No Macron's): ")
    if ask_7 == ANSWER_7:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{ANSWER_7}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_8 = input(f"What is the maori version of '{QUESTION_8}'? (No Macron's): ")
    if ask_8 == ANSWER_8:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{ANSWER_8}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_9 = input(f"What is the maori version of '{QUESTION_9}'? (No Macron's): ")
    if ask_9 == ANSWER_9:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{ANSWER_9}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_10 = input(f"What is the maori version of '{QUESTION_10}'? (No Macron's): ")
    if ask_10 == ANSWER_10:
        player += 1
        print()
        print("You got it right!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{ANSWER_10}'")
        print()

    return player


# Main Routine...
print("Welcome to The Maori Quiz! (Maori Numbers 1-10)")
print()

show_instructions = yes_no("Have you played this game before?: ")
print()

if show_instructions == "No":
    display_instructions()

else:
    exit()
