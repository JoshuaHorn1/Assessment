"""Maori Quiz Numbers Randomizer

"""

import random

maori_numbers = [["one", "tahi"], ["two", "rua"], ["three", "toru"],
                 ["four", "wha"], ["five", "rima"], ["six", "ono"],
                 ["seven", "whitu"], ["eight", "waru"], ["nine", "iwa"],
                 ["ten", "tekau"]]  # A list storing all the data for english and maori numbers 1-10

random = random.randint(1, 10)


print(f"What is {maori_numbers} in Maori?: ")
