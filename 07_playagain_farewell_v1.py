"""Maori Quiz Play again? / Farewell Code
(Developed without 02_yes_no_function_v1 and 06_questions_function_v1 implemented into this code)
"""

play_again = yes_no("Would you like to play again?").lower()  # asks the user if they want to play again
if play_again == "yes":  # if they say yes we redisplay questions
    questions()
else:
    print("Thanks for playing!\n"  # if they say no display formatted farewell text
          "I hope you had fun :D\n"
          "\n"
          "Goodbye!"
          "**********************\n"
          "----------------------\n"
          "######################")
