#!/usr/bin/python3
"""Module that returns a tuple with the length of a string and
its first character."""


def multiple_returns(sentence):
    """Return a tuple (length of sentence, first character).
    If sentence is empty, first character is None."""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
