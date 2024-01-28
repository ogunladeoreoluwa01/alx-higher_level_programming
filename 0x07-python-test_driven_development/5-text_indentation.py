#!/usr/bin/python3
"""This module contains a function able to print two new lines
after specified punctuation marks
"""


def text_indentation(text):
    """Print text with 2 newlines after ".", "?", or ":"

    Args:
        text (str): the text to be printed

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = False
    for i in range(len(text)):
        if text[i] != " ":
            flag = True
        if (text[i] == "." or text[i] == ":" or
                text[i] == "?" or text[i] == "\n"):
            print(f"{text[i]}\n")
            flag = False
        elif flag:
            print(text[i], end="")
