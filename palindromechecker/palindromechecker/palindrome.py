"""Determine whether or not an input string is a palindrome."""

# Reference:
# https://en.wikipedia.org/wiki/Palindrome


# implement to_chars(word: str) -> str:
""" Identifying & Checking that the letters in the palindrome are letters """

def to_chars(s):
    """Determine whether or not word is a palindrome."""
    s = s.lower()
    letters = " "
    for c in s:
        if c in "abcdefghijklmnopqrstuvwxyz":
            letters = letters + c
    return letters


# implement def is_palindrome_recursive(word: str) -> bool:
# --> "recursive": use the recursive approach described on page 129
def is_palindrome_recursive(s):
    """Assumes s is a str returns True if letters in s form a palindrome; False otherwise. Non-letters and capitalization are ignored."""
    # implement def is_palindrome(word: str) -> bool:
    """Determine whether or not word is palindrome"""

    def is_palindrome(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_palindrome(s[1:-1])

    return is_palindrome(to_chars(s))


# implement def is_palindrome_reverse(word: str) -> bool:
# --> "reverse": use the recursive approach described on page 164
def is_palindrome_reverse(s):
    """Assumes s is a str returns True if the str is a palindrome; False otherwise."""
    x = to_chars(s).split(" ")
    temp = x[:]
    temp.reverse()
    return temp == x
