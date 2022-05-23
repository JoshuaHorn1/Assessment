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

    # asks the user a question:
    ask_1 = input(f"What is the Maori version of "
                  f"'one (1)'? (No Macron's): ").lower()

    # if they get it right display total and
    # a congratulations message
    if ask_1 == "tahi":
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    # if they get it wrong display
    # the correct answer and total
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was 'Tahi'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    # Repeat for each question:
    ask_2 = input(f"What is the Maori version of "
                  f"'two (2)'? (No Macron's): ").lower()
    if ask_2 == "rua":
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was 'Rua'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_3 = input(f"What is the Maori version of "
                  f"'three (3)'? (No Macron's): ").lower()
    if ask_3 == "toru":
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was 'Toru'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_4 = input(f"What is the Maori version of "
                  f"'four (4)'? (No Macron's): ").lower()
    if ask_4 == "wha":
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was 'Wha'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_5 = input(f"What is the Maori version of "
                  f"'five (5)'? (No Macron's): ").lower()
    if ask_5 == "rima":
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was 'Rima'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_6 = input(f"What is the Maori version of "
                  f"'six (6)'? (No Macron's): ").lower()
    if ask_6 == "ono":
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was 'Ono'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_7 = input(f"What is the Maori version of "
                  f"'seven (7)'? (No Macron's): ").lower()
    if ask_7 == "whitu":
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was 'Whitu'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_8 = input(f"What is the Maori version of "
                  f"'eight (8)'? (No Macron's): ").lower()
    if ask_8 == "waru":
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The  correct answer was 'Waru'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_9 = input(f"What is the Maori version of "
                  f"'nine (9)'? (No Macron's): ").lower()
    if ask_9 == "iwa":
        player += 1
        print()
        print("You got it right!")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was 'Iwa'")
        print(f"You currently have a total of {player}/{TOTAL}!")
        print()

    ask_10 = input(f"What is the Maori version of "
                   f"'ten (10)'? (No Macron's): ").lower()
    if ask_10 == "tekau":
        player += 1
        print()
        print("You got it right!")
        print()
    else:
        print()
        print("Sorry, that's wrong")
        print(f"The correct answer was 'Tekau'")
        print()

    return player


# function to format text
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine...
# formatted welcome message
print(formatter("#", "Welcome to The Maori Quiz!"))
print()

# calls on the yes no function to answer a question
show_instructions = yes_no("Have you played this Quiz before?: ")
print()

# calls on the display instructions
# function if the user hasn't played before
if show_instructions == "No":
    display_instructions()

# creates a variable to count the total questions answered and calls
# on the questions function to display questions at the same time:
player_total = questions()

# keeps track of total and prints it
print(f"Your total was {player_total}/{TOTAL}!")
if player_total <= 3:
    print()
    # displays a different message
    # depending on how well the user did;
    print(formatter("+", "Practice makes perfect!"))
elif player_total <= 7:
    print()
    print(formatter("+", "Good effort!"))
else:
    print()
    print(formatter("%", "WOW! You did amazing!"))

print()
# asks the user if they want to play again
play_again = yes_no("Would you like to play again?: ").lower()
print()
if play_again == "yes":  # if they say yes we redisplay questions
    questions()
else:
    # if they say no display formatted farewell text
    print(formatter("*", "Thanks for playing!"))
    print()
    print("I hope you had fun :D\n"
          "\n")
    print(formatter("$", "Goodbye!"))
