"""
Problem statement
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

def is_unique(string):
    """
    Returns boolean indicating if the string has unique characters or not
    """
    unique_chars = set()
    for char in string:
        if char in unique_chars:
            print(f"char {char} is repeated")
            return False
        else:
            unique_chars.add(char)               
    return True
