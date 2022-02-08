# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

def swap_first_last(sen):
    if len(sen) < 2:
        return sen
    new_sen = sen[-1] + sen[1:-1] + sen[0]
    return new_sen


def test_swap_first_last():
    assert swap_first_last("I love you") == "u love yoI"
    assert swap_first_last("delete this item") == "melete this ited"
    assert swap_first_last("de") == "ed"
    assert swap_first_last("d") == "d"
    assert swap_first_last("") == ""
