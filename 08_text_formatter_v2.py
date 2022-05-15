"""Maori Quiz - Text formatter v2
Turns code from 08_text_formatter_v1 into a function that can
be integrated into base code.
"""


# function to format text
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("-", "Welcome to the Maori Quiz!"))
print()
print(formatter("!", "What is the Maori version of 'one'? "))
print()
print(formatter("*", "Goodbye"))
