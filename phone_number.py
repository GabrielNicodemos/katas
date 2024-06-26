"""
    Write a function that accepts an array of 10 integers (between 0 and 9),
    that returns a string of those numbers in the form of a phone number.

    Example: create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""
def create_phone_number(n):
    n_string = ''.join(map(str, n))

    return f'({n_string[0:3]}) {n_string[3:6]} - {n_string[6:10]}'