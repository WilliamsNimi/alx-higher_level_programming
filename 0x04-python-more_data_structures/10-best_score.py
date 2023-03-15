#!/usr/bin/python3


def best_score(a_dictionary):
    maxi = 0
    for key, values in a_dictionary.items():
        if values > maxi:
            maxi = values
            max_key = key
    return max_key
