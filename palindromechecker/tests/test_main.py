# Add the required docstring and any required imports of objects
"""Test the functions in the main.py file."""
import typer
from palindromechecker import __version__

from typer.testing import CliRunner

runner = CliRunner()

cli = typer.Typer()

# Reference:
# https://typer.tiangolo.com/tutorial/testing/


def test_palindromechecker_recursive_is_palindrome():
    """Ensure that the command-line interface works for recursive approach."""
    result = runner.invoke(cli, ["--word", "civic", "--approach", "recursive"])
    assert result.exit_code == 0
    assert "recursive" in result.stdout
    assert "reverse" not in result.stdout
    assert "Yes, it is!" in result.stdout
    assert "civic" in result.stdout


def test_palindromechecker_recursive_is_not_palindrome():
    """Ensure that the command-line interface works for recursive approach."""
    # implement this test case using the provided example
    result = runner.invoke(cli, ["--word", "civic", "--approach", "recursive"])
    assert result.exit_code == 0
    assert "recursive" not in result.stdout
    assert "reverse" in result.stdout
    assert "Yes, it is!" not in result.stdout
    assert "civic" not in result.stdout


def test_palindromechecker_reverse_is_palindrome():
    """Ensure that the command-line interface works for reverse approach."""
    # TODO: implement this test case using the provided example


def test_palindromechecker_reverse_is_not_palindrome():
    """Ensure that the command-line interface works for reverse approach."""
    # TODO: implement this test case using the provided example