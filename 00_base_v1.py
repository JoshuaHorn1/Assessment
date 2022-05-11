"""Maori Quiz (Numbers 1-10) Base code
Components added after testing/trialling
- Has the yes/no checking function
- Has instructions displaying function
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


# Main Routine...
print("Welcome to The Maori Quiz! (Maori Numbers 1-10)")
print()

show_instructions = yes_no("Have you played this game before?: ")
print()

if show_instructions == "No":
    display_instructions()

else:
    exit()
