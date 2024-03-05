#!/usr/bin/python3i
""" Definition """


def write_file(filename="", text=""):
    """ printing"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
