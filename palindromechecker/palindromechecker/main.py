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
# TODO: define a PalindromeCheckingApproach enumeration with these options:
# --> "recursive": use the recursive approach described on page 129
def is_palindrome(s):
    """Assumes s is a string returns true if letters in s form a palindrome; False otherweise. Non-letters and capitalization are ignored."""

    def to_chars(s):
        s = s.lower()
        letters = ' '
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
# --> "reverse": use the recursive approach described on page 164
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))
# TODO: implement a command-line interface using typer that produces
# output like those examples included in the remainder of this file
@cli.command()
def palindromechecker(
    approach: str = typer.Option(...),
    word: str = typer.Option(...),
):
    """Determine if the word is a palindrome through the specified approach."""
    # create a console for rich text output
    console = Console()
    # display the debugging output for the program's command-line arguments
    console.print("")
    console.print(f":sparkled: Awesome, using the {approach} for palindrome checking!")
    console.print("")
    console.print(
        f":abacus: Going to check to see if the word {word} is a palindrome!"
    )

    console.print("")
    # construct the full name of the function to call
    Profiler.start()
    start = time.time()
    palindrome_checker = is_palindrome(word)
    end = time.time()
    Profiler.stop()
    # display debugging information with the function's output
    # display a final message and some extra spacing, asking a question
    # about the efficiency of the approach to computing the number sequence
    console.print(
        "🤷 So, is this word a palindrome?"
    )
    console.print("")
    process = psutil.Process(os.getpid())
    # display a simplified execution time
    # Reference:
    # https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
    console.print("Estimated execution time according to the simple timer:")
    console.print(f"    {(end - start):.2f} seconds")
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
