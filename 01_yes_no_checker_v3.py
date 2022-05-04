"""Maori Quiz Yes / No checker v3 - based on v2
puts the code from Yes / No checker v2 into a loop for testing purposes
"""

# welcome note:
print("Welcome to The Maori Quiz! (Maori Numbers 1-10)")
print()

show_instructions = ""
while show_instructions != "x":

    # Ask the user if they have played before
    show_instructions = input("Have you played this Quiz before? (Yes/No): ").lower()

    # if they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    # if they say no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")

    # otherwise - show error
    else:
        print("Please answer 'Yes (Y)' or 'No (N)'")

    print(f"You entered '{show_instructions}'")
