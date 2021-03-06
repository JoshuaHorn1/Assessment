"""Maori Quiz Yes / No checker v2 - based on v1
simplifies the input by converting it to a lower case. also accepts y or n as
abbreviations. prints result of users choice as input - for testing
adds welcome note
"""

# welcome note:
print("Welcome to The Maori Quiz! (Maori Numbers 1-10)")
print()

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

