#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length_sentence = len(sentence)
        first_character = sentence[0]
    else:
        length_sentence = len(sentence)
        first_character = "None"
    return(length_sentence, first_character)
