# Add the required docstring and any required imports of objects
"""Test case for palindrome file."""
import typer
from palindromechecker import __version__

from typer.testing import CliRunner

runner = CliRunner()

cli = typer.Typer()

# Reference:
# https://docs.pytest.org/en/6.2.x/


def test_short_palindrome_word_recursive():
    """Ensure that a short word of "civic" works correctly."""
    word = "civic"
    result = palindrome.is_palindrome_recursive(word)
    assert result is True


def test_short_not_palindrome_word_recursive():
    """Ensure that a short word of "taylor" does not work correctly."""
    # implement this test case using the provided example
    word = "civic"
    result = palindrome.is_palindrome_recursive(word)
    assert result is False


def test_short_palindrome_word_reverse():
    """Ensure that a short word of "civic" works correctly."""
    # TODO: implement this test case using the provided example


def test_short_not_palindrome_word_reverse():
    """Ensure that a short word of "taylor" does not work correctly."""
    # TODO: implement this test case using the provided example
