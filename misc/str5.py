# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


def word_endings(word):
    result = ""
    if len(word) >= 3:
        if word[-3:] == "ing":
            result = word + "ly"
        elif word[-2:] == "ly":
            result = word
        else:
            result = word + "ing"
    else:
        result = word
    return result


def test_endings():
    assert word_endings('abc') == 'abcing'
    assert word_endings('string') == 'stringly'
    assert word_endings('st') == 'st'
    assert word_endings('strongly') == 'strongly'
