#!/usr/bin/python3


def roman_to_int(roman_string):
    new_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    sum_ = 0
    if roman_string is None and !isinstance(roman_string, str):
        return 0
    for i in range(0, len(roman_string)):
        if i > 0:
            if roman_string[i] == 'V' or roman_string[i] == 'X':
                if roman_string[i - 1] == 'I':
                    sum_ = sum_ + new_dict[roman_string[i]] - 2
                else:
                    sum_ = sum_ + new_dict[roman_string[i]]
            else:
                sum_ = sum_ + new_dict[roman_string[i]]
        else:
            sum_ = sum_ + new_dict[roman_string[i]]
    return sum_
