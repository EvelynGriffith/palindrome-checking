# Add the required docstring for this module
"""implement the test for the human readable boolean function."""

# implement the def get_human_readable_boolean(answer: bool) -> str function
def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # produce a human-readable value for a bool
    # True --> "Yes"
    # False --> "No"
    # originally had if answer != True:
    # Flake8 Linting Tool said it needed to be is not instead of !=
    # therefore it needed changed to have a passing build
    """ note that the build failed if we used != True instead of is not True """
    if answer is not True:
        return "No, it is not!"
    else:
        return "Yes, it is!"
