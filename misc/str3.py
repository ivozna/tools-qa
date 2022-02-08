# Write a Python program to get a string from a given string where all occurrences
# of its first char have been changed to '$', except the first char itself.

def dollar_task(text):
    result = text
    for index in range(1, len(result)):
        item = result[index]
        if item == result[0]:
            result = result[:index] + "$" + result[index+1:]
    return result







def test_dollar_task():
    assert dollar_task('restart') == 'resta$t'
    assert dollar_task('mamma mia') == 'ma$$a $ia'
    assert dollar_task('') == ''
