# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String


def new_string(text):
    if len(text) < 2:
        return ""
    result = text[0] + text[1] + text[-2] + text[-1]
    return result


def test_new_string():
    assert new_string('w3resource') == 'w3ce'
    assert new_string('w3') == 'w3w3'
    assert new_string('w') == ""
