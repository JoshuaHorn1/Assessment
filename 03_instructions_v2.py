"""Maori Quiz Instructions code v2
Adds some formatting to instruction displaying code
(This version was developed without the yes/no function implemented into it)
"""

# Main Routine...
show_instructions = yes_no("Have you played this game before?: ")
print(f"You entered '{show_instructions}'")

if show_instructions == "Yes":
    print("Welcome to The Maori Quiz!\n"
          "\n"
          "Instructions to display will go here\n"
          "\n"
          "Program continues\n")

else:
    print("Program continues.")
