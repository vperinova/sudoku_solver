class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class SolutionError(Error):

    def __init__(self, n, condition, text):
        self.number = n
        self.condition = condition
        self.message = text

class SolutionError0(Error):
    def __init__(self, text):
        self.message = text
