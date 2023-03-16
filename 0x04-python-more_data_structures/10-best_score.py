#!/usr/bin/python3


def best_score(a_dictionary):
    if not (a_dictionary):
        return None
    else:
        maxi = 0
        max_key = ""
        for key, values in a_dictionary.items():
            if values > maxi:
                maxi = values
                max_key = key
        return max_key
    return None
