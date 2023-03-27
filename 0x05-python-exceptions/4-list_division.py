#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    c = 0
    for i in range(0, list_length):
        try:
            c = my_list_1[i] / my_list_2[i]
            new_list[i] = c
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            c = 0
    return new_list
