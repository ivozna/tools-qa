# Write a Python program to remove the nth index character from a nonempty string.


def nth_index(word, index):

    new_word = word[:index] + word[index+1:]
    return new_word


def test_nth_index():
    assert nth_index("hedgehog", 0) == "edgehog"
