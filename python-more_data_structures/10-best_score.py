#!/usr/bin/python3
def best_score(a_dictionary):
    high_score = []
    if a_dictionary:
        best_key = max(a_dictionary.keys())
        return best_key
    else:
        return None
