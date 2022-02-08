# Write a Python function that takes a list of words
# and return the longest word and the length of the longest one. Go to the editor
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

def longest_word(lst):
    lst = sorted(lst, key=len, reverse=True)
    return lst[0], len(lst[0])












def test_longest_word():
    assert longest_word(["me", "you", "name", "flower", "exercises"]) == ("exercises", 9)
    assert longest_word(["me", "you", "name", "flower"]) == ("flower", 6)
    assert longest_word(["me"]) == ("me", 2)
    assert longest_word([""]) == ("", 0)

