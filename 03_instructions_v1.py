"""Maori Quiz Instructions code v1
Code used to display instructions - will be used with 02_yes_no_function_v1
(This version was developed without the yes/no function implemented into it)
"""

# Main Routine...
show_instructions = yes_no("Have you played this game before?: ")
print(f"You entered '{show_instructions}'")

if show_instructions == "Yes":
    print("Welcome to The Maori Quiz!")
    print()
    print("instructions to display will go here")
    print()
    print("Program continues.")

else:
    print("Program continues.")
