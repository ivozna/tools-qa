# Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


sen = "google.com"
result = {}
for letter in sen:
    if letter in result:
        result[letter] += 1
    else:
        result[letter] = 1
    # result[letter] = result.get(letter, 0) + 1

print(result)
