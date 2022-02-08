import time


def linear_search(lst, x):
    for number in lst:
        if x == number:
            return True
    return False


def test_linear_search():
    assert linear_search(lst=range(1, 100000), x=67000) == True
    assert linear_search(lst=range(1, 100000), x=100001) == False
    assert linear_search([], 11) == False
    assert linear_search([], 0) == False

def binary_search(lst, x, left, right):
    if left == right:
        return False
    mid = int((left + right) / 2)
    if x == lst[mid]:
        return True
    if x < lst[mid]:
        return binary_search(lst, x, left, mid - 1)
    if x > lst[mid]:
        return binary_search(lst, x, mid + 1, right)


def test_binary_search():
    assert binary_search(range(1, 100000), 67000, 0, 99999) == True
    assert binary_search(range(1, 100000), 8888888888, 0, 99999) == False
    assert binary_search([], 11, 0, 0) == False
    assert binary_search([], 0, 0, 0) == False


def while_binary_search(lst, x):
    left = 0
    right = len(lst) - 1
    while right >= left:
        mid = int((left + right) / 2)
        if x == lst[mid]:
            return True
        if x < lst[mid]:
            right = mid - 1
        elif x > lst[mid]:
            left = mid + 1
    return False



def test_while_binary_search():
    assert while_binary_search(range(1, 10), 9) == True
    # assert while_binary_search(range(1, 100000), 8888888888) == False
    # assert while_binary_search([], 11) == False
    # assert while_binary_search([], 0) == False
    #

