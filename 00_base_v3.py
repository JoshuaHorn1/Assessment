"""Maori Quiz (Numbers 1-10) Base code
Components added after testing/trialling
- Has the yes/no checking function
- Has instructions displaying function
- Has the questions/answers
- Has "play again/farewell note"
- Includes text formatter and welcome note
- Formats general text
"""

# Variables go here...

TOTAL = 10
player_total = 0

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
    print(formatter("-", "How to play:"))
    print("\n"
          "You will be asked a series of questions\n"
          "on english numbers to which you will have\n"
          "to say the Maori equivalent on it (No Macrons)\n"
          "\n"
          "You will be scored out of 10, and at the end\n"
          "you will be prompted if you wish to try again\n"
          "or quit the program.\n")
    print(formatter("!", "Good luck, and have fun!"))
    print()


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

    ask_1 = input(f"What is the maori version of '{question_1}'? (No Macron's): ").lower()  # asks the user a question
    if ask_1 == answer_1:  # if they get it right display total and congratulations message
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:  # if they get it wrong display the correct answer and total
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{answer_1}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_2 = input(f"What is the maori version of '{question_2}'? (No Macron's): ").lower()
    if ask_2 == answer_2:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{answer_2}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_3 = input(f"What is the maori version of '{question_3}'? (No Macron's): ").lower()
    if ask_3 == answer_3:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{answer_3}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_4 = input(f"What is the maori version of '{question_4}'? (No Macron's): ").lower()
    if ask_4 == question_4:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{answer_4}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_5 = input(f"What is the maori version of '{question_5}'? (No Macron's): ").lower()
    if ask_5 == answer_5:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{answer_5}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_6 = input(f"What is the maori version of '{question_6}'? (No Macron's): ").lower()
    if ask_6 == answer_6:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{answer_6}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_7 = input(f"What is the maori version of '{question_7}'? (No Macron's): ").lower()
    if ask_7 == answer_7:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{answer_7}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_8 = input(f"What is the maori version of '{question_8}'? (No Macron's): ").lower()
    if ask_8 == answer_8:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The  correct answer was '{answer_8}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_9 = input(f"What is the maori version of '{question_9}'? (No Macron's): ").lower()
    if ask_9 == answer_9:
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{answer_9}'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_10 = input(f"What is the maori version of '{question_10}'? (No Macron's): ").lower()
    if ask_10 == answer_10:
        player += 1
        print()
        print("You got it right!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was '{answer_10}'")
        print()

    return player


# function to format text
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine...
print(formatter("#", "Welcome to The Maori Quiz!"))
print()

show_instructions = yes_no("Have you played this Quiz before?: ")
print()

if show_instructions == "No":
    display_instructions()

player_total = questions()
print(f"Your total was {player_total}/{TOTAL}!")
if player_total <= 3:
    print()
    print(formatter("+", "Practice makes perfect!"))
elif player_total <= 7:
    print()
    print(formatter("+", "Good effort!"))
else:
    print()
    print(formatter("%", "WOW! You did amazing!"))

print()
play_again = yes_no("Would you like to play again?: ").lower()  # asks the user if they want to play again
print()
if play_again == "yes":  # if they say yes we redisplay questions
    questions()
else:
    print(formatter("*", "Thanks for playing!"))  # if they say no display formatted farewell text
    print()
    print("I hope you had fun :D\n"
          "\n")
    print(formatter("$", "Goodbye!"))
