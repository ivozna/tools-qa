# Write a Python program to remove the characters which have odd index values of a given string.

def remove_odds(text):
    new_text = []
    for index, value in enumerate(text):
        if index % 2 == 0:
            new_text.append(value)
    return ''.join(new_text)


def test_remove_odds():
    assert remove_odds("computers and laptops") == "cmuesadlpos"
