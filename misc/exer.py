# Please write a program which count and print the numbers of each character in a string input by console.
# Example:
# If the following string is given as input to the program: abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

def character_count(sen):
    """documentation ghghhgh
    hghghhghgh
    jfjgjjgjjg """
    dic = {}
    for letter in sen:
        dic[letter] = dic.get(letter, 0) + 1

    return dic

print(character_count.__doc__)

# def test_character_count():
#     assert character_count("abcdefgabc") == {'a': 2, 'b': 2, 'c': 2, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
#     assert character_count("a") == {'a': 1}
#     assert character_count("") == {}
