"""Maori Quiz - Text formatter v1
A function that takes a symbol and text input
and presents the text in a nicer way
"""


# function to format output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
text1 = input("Enter the statement you want to format: ")
symbol1 = input("What symbol do you want to use: ")
print()
print(formatter(symbol1, text1))
