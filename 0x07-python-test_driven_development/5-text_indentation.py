#!/usr/bin/python3


def text_indentation(text):
    """ this is a text_indentation function """
    if type(text) != str:
        raise TypeError("text must be a string")
    for character in text:
        if character == '?' or character == ':':
            print("")
            print("")
        else:
            print(character, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt", optionflags=ELLIPSIS)
