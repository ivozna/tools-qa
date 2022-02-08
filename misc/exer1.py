#Write a Python script to sort a dictionary (ascending and descending) by value.
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
dic = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0, 10: 4, 11: 4}

# sorted_values = sorted(dic.values())
# result = {}
#
# for value in sorted_values:
#     for key in dic:
#         if dic[key] == value:
#             result[key] = value
#
#
# print(result)

sorted_values = sorted(dic.values(), reverse=True)
result = {}

for value in sorted_values:
    for key in dic:
        if dic[key] == value:
            result[key] = value


print(result)