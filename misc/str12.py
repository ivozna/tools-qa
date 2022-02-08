# Write a Python program to wrap a given string into a paragraph of given width. Go to the editor
# Sample Output:
# Input a string: The quick brown fox.
# Input the width of the paragraph: 10
# Result:
# The quick
# brown fox.

#
# def width_string(text, width):
#     results = []
#     for i in range(0, len(text), width):
#         results.append(text[i:i + 10])
#     return "\n".join(results)
#
#
# def test_width_string():
#     assert width_string("The quick brown fox", 10) == "The quick \nbrown fox"
from textwrap import wrap


def width_string(text, width):
    result = (wrap(text, width))
    return " \n".join(result)

def test_width_string():
    assert width_string("The quick brown fox", 10) == "The quick \nbrown fox"
