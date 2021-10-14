# provide a descriptive docstring for the module
"""Contain the CLI function, and allow the program to run all methods of approach."""

# import all of the required packages and modules
import typer

from enum import Enum

from rich.console import Console

from palindromechecker import palindrome

# create the command-line interface object with typer
cli = typer.Typer()

# define a PalindromeCheckingApproach enumeration with these options:
# --> "recursive": use the recursive approach described on page 129
# --> "reverse": use the recursive approach described on page 164

class PalindromeCheckerApproach(Str, Enum):
    """Define the name for the approach for performing palindrome checking."""

    recursive = "recursive"
    reverse = "reverse"

# TODO: implement a command-line interface using typer that produces
# output like those examples included in the remainder of this file
@cli.command()
def palindrome(
    word: str = typer.option(...),
    approach: PalindromeCheckerApproach = PalindromeCheckerApproach.recursive,
) -> None:
    """Use iteration to perform primality testing on a number and run a profiling data collection if requested."""
    # create a console for rich text output
    console = Console()
    # create an empty primality_tuple
    primality_tuple: Tuple[bool, List[int]]
    if approach.value == PalindromeCheckerApproach.recursive:
        is_palindrome_recursive = palindrome.is_palindrome_recursive(word)
    elif approach.value == PalindromeCheckerApproach.reverse:
        is_palindrome_reverse = palindrome.is_palindrome_reverse(word)
        # Reference for more details:
        # https://github.com/joerick/pyinstrument
        # perform profiling on the execution of the primality test
       
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
