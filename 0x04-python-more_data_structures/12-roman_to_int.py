#!/usr/bin/python3
# Function to convert Roman numerals to integers

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
                 'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000
                 }
    integer = 0
    prev_value = 0

    for c in roman_string:
        value = roman_dict.get(c, 0)
        if value == 0:
            return 0

        if prev_value < value:
            integer -= prev_value
        else:
            integer += prev_value

        prev_value = value

    integer += prev_value

    return integer
