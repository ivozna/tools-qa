# Write a Python program to count the occurrences of each word in a given sentence.


def word_occurences_count(sen):
    dic = {}
    splitted_sen = sen.split()
    for word in splitted_sen:
        dic[word] = dic.get(word,0) +1

    return dic


def test_word_occurences_count():
    assert word_occurences_count("Process finished with exit code with exit code") == {"Process": 1, "finished": 1,
                                                                                       "with": 2, "exit": 2,
                                                                                       "code": 2}
