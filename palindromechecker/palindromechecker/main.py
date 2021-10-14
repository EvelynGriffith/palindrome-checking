# provide a descriptive docstring for the module
"""Contain the CLI function, and allow the program to run all methods of approach."""

# TODO: import all of the required packages and modules
from pyinstrument import Profiler  # type: ignore

import typer

from rich.console import Console

import os
import psutil  # type: ignore
import time
# create the command-line interface object with typer
cli = typer.Typer()

class PalindromeCheckerApproach(Str, Enum):
    """Define the name for the approach for performing palindrome checking."""

    recursive = "recursive"
    reverse = "reverse"

# TODO: define a PalindromeCheckingApproach enumeration with these options:
# --> "recursive": use the recursive approach described on page 129
def recursive_is_palindrome(s):
    """Assumes s is a string returns true if letters in s form a palindrome; False otherweise. Non-letters and capitalization are ignored."""

    def to_chars(s):
        s = s.lower()
        letters = ' '
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))
# --> "reverse": use the recursive approach described on page 164
def reverse_is_pal(s):
    temp = s[:]
    temp.reverse()
    return temp == s
# TODO: implement a command-line interface using typer that produces
# output like those examples included in the remainder of this file
@cli.command()
def primality(
    word: str = typer.option(...),
    approach: PalindromeCheckerApproach = PalindromeCheckerApproach.recursive,
) -> None:
    """Use iteration to perform primality testing on a number and run a profiling data collection if requested."""
    # create a console for rich text output
    console = Console()
    # create an empty primality_tuple
    primality_tuple: Tuple[bool, List[int]]
    if approach.recursive == PalindromeCheckerApproach.recursive:
        # Reference for more details:
        # https://github.com/joerick/pyinstrument
        # perform profiling on the execution of the primality test
        if profile:
            profiler.start()
            # use the efficient primality testing algorithm
            primality_tuple = primality_test_efficient(number)
            # do not perform profiling
            profiler.stop()
        else:
            primality_tuple = primality_test_efficient(number)
    elif approach.value == PrimalityTestingApproach.exhaustive:
        # Reference for more details:
        # https://github.com/joerick/pyinstrument
        # perform profiling on the execution of the primality test
        if profile:
            profiler.start()
            # use the exhaustive primality testing algorithm
            primality_tuple = primality_test_exhaustive(number)
            # do not perform profiling
            profiler.stop()
        else:
            primality_tuple = primality_test_exhaustive(number)
            # display the results of the primality test
   
 was_prime_found = primality_tuple[0]
    divisor_list = primality_tuple[1]
    console.print(f":smile: Attempting to determine if {number} is a prime number!")
    console.print()
    console.print(
        f":sparkles: What divisors were found? {pretty_print_list(divisor_list)}"
    )
    console.print(
        f":sparkles: Was this a prime number? {human_readable_boolean(was_prime_found)}"
    )
    # display the results of the profiling if that option was requested
    if profile:
        console.print()
        console.print(
            f":microscope: Here's profile data from performing primality testing on {number}!"
        )
        profiler.print()
# poetry run palindromechecker --help

# Usage: palindromechecker [OPTIONS]
#
#   Use a method to determine if an input string is a palindrome or not.
#
# Options:
#   --word TEXT                     [required]
#   --approach [recursive|reverse]  [default: reverse]
#   --install-completion            Install completion for the current
#                                   shell.
#
#   --show-completion               Show completion for the current shell,
#                                   to copy it or customize the
#                                   installation.
#
#   --help                          Show this message and exit.

# poetry run palindromechecker --word civic --approach recursive

# ✨ Awesome, using the recursive approach for palindrome checking!

# 🔖 Going to check to see if the word "civic" is a palindrome!

# 😆 Is this word a palindrome? Yes, it is!
