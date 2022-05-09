"""Maori Quiz Questions/Randomizer v1
Randomizes a list containing the maori numbers and answers
and then prints evidence of its randomization
"""

import random

maori_numbers = [["one", "tahi"], ["two", "rua"], ["three", "toru"],
                 ["four", "wha"], ["five", "rima"], ["six", "ono"],
                 ["seven", "whitu"], ["eight", "waru"], ["nine", "iwa"],
                 ["ten", "tekau"]]  # A list storing all the data for english and maori numbers 1-10

random.shuffle(maori_numbers)  # shuffles the contents of the list

print(maori_numbers)  # prints the randomized list as evidence it works
