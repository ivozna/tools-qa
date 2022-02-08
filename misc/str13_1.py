# Write a Python script that takes input from the user and displays that input back in upper and lower cases.



def upper_lower(text):
    upper = text.upper()
    lower = text.lower()
    return [upper, lower]


def test_upper_lower():
    assert upper_lower("Launching") == ["LAUNCHING", "launching"]
