"""Determine whether or not an input string is a palindrome."""

# Reference:
# https://en.wikipedia.org/wiki/Palindrome

# implement to_chars(word: str) -> str:
def to_chars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

def is_palindrome_recursive(s):
    """ Assumes s is a str
    Returns True if letters in s form a palindrome; False
    otherwise. Non-letters and capitalization are ignored. """

    # implement def is_palindrome(word: str) -> bool:
    def is_palindrome(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_palindrome(s[1:-1])

    return is_palindrome(to_chars(s))

def is_palindrome_reverse(s):
    """ Assumes s is a str
    Returns True if the str is a palindrome; False otherwise"""
    x = to_chars(s).split('')
    temp = x[:]
    temp.reverse()
    return temp == x