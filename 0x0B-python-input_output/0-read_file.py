#!/usr/bin/python3i
""" Definition """


def read_file(filename=""):
    """ printing"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
