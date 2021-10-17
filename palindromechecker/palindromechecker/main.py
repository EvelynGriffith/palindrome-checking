# provide a descriptive docstring for the module
"""Contain the CLI function, and allow the program to run all methods of approach."""

# import all of the required packages and modules
import typer

from enum import Enum


from rich.console import Console

from palindromechecker import palindrome

from palindromechecker import util

# create the command-line interface object with typer
cli = typer.Typer()

# define a PalindromeCheckingApproach enumeration with these options:
# --> "recursive": use the recursive approach described on page 129
# --> "reverse": use the recursive approach described on page 164


class PalindromeCheckingApproach(str, Enum):
    """Define the name for the approach for performing palindrome checking."""

    recursive = "recursive"
    reverse = "reverse"


# implement a command-line interface using typer that produces
# output like those examples included in the remainder of this file
@cli.command()
def palindrome_one(
    word: str = typer.Option(...),
    approach: PalindromeCheckingApproach = PalindromeCheckingApproach.recursive,
) -> None:
    """Use iteration to perform primality testing on a number and run a profiling data collection if requested."""
    # create a console for rich text output
    console = Console()
    # create an empty primality_tuple
    # primality_tuple: Tuple[bool, List[int]]
    if approach.value == PalindromeCheckingApproach.recursive:
        found_if_palindrome = palindrome.is_palindrome_recursive(word)
    elif approach.value == PalindromeCheckingApproach.reverse:
        found_if_palindrome = palindrome.is_palindrome_reverse(word)

    console.print(f":Sparkles: Awesome. using the {approach} for palindrome checking!")
    console.print()
    console.print(
        f":bookmark: Going to check to see if the word {word} is a palindrome!"
    )
    console.print()
    console.print(
        f":satisfied: Is this word a palindrome? {util.human_readable_boolean(found_if_palindrome)}"
    )


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
