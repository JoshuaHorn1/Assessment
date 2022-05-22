"""Maori Quiz (Numbers 1-10) Final Program.
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

    ask_1 = input(f"What is the Maori version of 'one (1)'? (No Macron's): ").lower()  # asks the user a question
    if ask_1 == "tahi":  # if they get it right display total and congratulations message
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

    ask_2 = input(f"What is the Maori version of 'two (2)'? (No Macron's): ").lower()
    if ask_2 == "rua":
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

    ask_3 = input(f"What is the Maori version of 'three (3)'? (No Macron's): ").lower()
    if ask_3 == "toru":
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

    ask_4 = input(f"What is the Maori version of 'four (4)'? (No Macron's): ").lower()
    if ask_4 == "wha":
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

    ask_5 = input(f"What is the Maori version of 'five (5)'? (No Macron's): ").lower()
    if ask_5 == "rima":
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

    ask_6 = input(f"What is the Maori version of 'six (6)'? (No Macron's): ").lower()
    if ask_6 == "ono":
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

    ask_7 = input(f"What is the Maori version of 'seven (7)'? (No Macron's): ").lower()
    if ask_7 == "whitu":
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

    ask_8 = input(f"What is the Maori version of 'eight (8)'? (No Macron's): ").lower()
    if ask_8 == "waru":
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

    ask_9 = input(f"What is the Maori version of 'nine (9)'? (No Macron's): ").lower()
    if ask_9 == "iwa":
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

    ask_10 = input(f"What is the Maori version of 'ten (10)'? (No Macron's): ").lower()
    if ask_10 == "tekau":
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
print(formatter("#", "Welcome to The Maori Quiz!"))  # formatted welcome message
print()

show_instructions = yes_no("Have you played this Quiz before?: ")  # calls on the yes no function to answer a question
print()

if show_instructions == "No":  # calls on the display instructions function if the user hasn't played before
    display_instructions()

# creates a variable to count the total questions answered and calls
# on the questions function to display questions at the same time:
player_total = questions()
print(f"Your total was {player_total}/{TOTAL}!")  # keeps track of total and prints it
if player_total <= 3:
    print()
    print(formatter("+", "Practice makes perfect!"))   # displays a different message depending on how well the user did;
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
