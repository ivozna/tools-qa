# [1, 10, [15, [25,5, [1,5,5]]], 14, [1, [2,3],4,[6,6,[7]]]]
# [1,10,51, 14, ... ]


def level(lst):
    new_lst = []
    for elem in lst:
        if isinstance(elem, int):
            new_lst.append(elem)
        if isinstance(elem, list):
            new_lst.append(sum(elem))
    return new_lst


def test_level():
    assert level([5, 10, [15, 25, 45], 10, [25, 35, 45], -100, 25, -1, 50, [1, -1, 1, 1, 1]]) == [5, 10, 85, 10, 105,

                                                                                                  -100, 25, -1, 50, 3]


def deep_sum(lst):
    sum = 0
    for elem in lst:
        if isinstance(elem, int):
            sum += elem
        if isinstance(elem, list):
            sum += deep_sum(elem)
    return sum


def flat(lst):
    new_lst = []
    for elem in lst:
        if isinstance(elem, int):
            new_lst.append(elem)
        if isinstance(elem, list):
            new_lst.append(deep_sum(elem))
    return new_lst


def test_flat():
    assert flat([1, 10, [10, [25, 5, [1, 5, 5]]], 14, [1, [2, 3], 4, [6, 6, [7]]]]) == [1, 10, 51, 14, 29]
