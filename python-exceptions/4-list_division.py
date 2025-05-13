#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            to_add = my_list_1[i] / my_list_2[i]
        except IndexError:
            to_add = 0
            print("out of range")
        except ZeroDivisionError:
            to_add = 0
            print("division by 0")
        except TypeError:
            to_add = 0
            print("wrong type")
        finally:
            new_list.append(to_add)
    return new_list
