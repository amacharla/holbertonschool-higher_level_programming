#!/usr/bin/python3
def text_indentation(text):
    """ Print text with 2 new lines after each special delimiter
    Arguments:
        text: string
    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.replace(". ", ".\n\n")
    text = text.replace("? ", "?\n\n")
    text = text.replace(": ", ":\n\n")
    print(text)
