"""Maori Quiz Yes / No checker v1
simple code developed for asking user if they have played
before or not - and shows error if an unexpected variable is typed
"""

# Ask the user if they have played before
show_instructions = input("Have you played this quiz before? (Yes/No): ")

# if they say yes, output 'program continues'
if show_instructions == "yes":
    print("Program continues")

# if they say no, output 'display instructions'
elif show_instructions == "no":
    print("Display instructions")


# otherwise - show error
else:
    print("Please answer 'Yes (Y)' or 'No (N)'")
