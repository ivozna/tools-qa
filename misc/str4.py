# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.


def swap(text1, text2):
    text1_new = text2[:2] + text1[2:]
    text2_new = text1[:2] + text2[2:]

    return text1_new + " " + text2_new


def test_swap():
    assert swap('abc', "xyz") == "xyc abz"
    assert swap('google', "facebook") == "faogle gocebook"
    assert swap('a', "x") == "x a"
    assert swap('', "xyz") == "xy z"

