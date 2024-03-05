#!/usr/bin/python3
"""Definition """


def append_write(filename="", text=""):
    """returns the number of characters added"""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
