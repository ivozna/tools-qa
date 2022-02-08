# Write a Python program to find the first appearance of the substring 'not' and 'poor'
# from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def not_poor(text):
    pos_not = text.find("not")
    pos_poor = text.find("poor")
    if pos_not == -1 or pos_poor == -1:
        return text
    if pos_not < pos_poor:
        return text[:pos_not] + "good" + text[pos_poor + 4:]
    return text





def test_not_poor():
    assert not_poor('The lyrics is not that poor!') == 'The lyrics is good!'
    assert not_poor('The lyrics is poor!') == 'The lyrics is poor!'
    assert not_poor('') == ''
    assert not_poor('The lyrics is poor not really.') == 'The lyrics is poor not really.'
