"""
This module provides functionality to parse Formula objects from their string representations.
It is primarily used for internal testing purposes.
"""



from .structure import Variable, Not, And, Or, Implication, Biconditional, Truth, Falsity, Next, Finally, Globally, Until, Release


def parse(expression):
    """
    Parse a string representation of a Formula object into an actual Formula object.

    @param expression: A string representation of a Formula object
    @return: The corresponding Formula object
    """


    def safe_eval(expr):
        """
        Safely evaluate a string expression to create a Formula object.

        @param expr: A string expression representing a Formula
        @return: The corresponding Formula object
        """
        
        def variable(name):
            return Variable(name.strip("'"))

        def not_op(operand):
            return Not(operand)

        def and_op(left, right):
            return And(left, right)

        def or_op(left, right):
            return Or(left, right)

        def implication(left, right):
            return Implication(left, right)

        def biconditional(left, right):
            return Biconditional(left, right)

        def truth():
            return Truth()

        def falsity():
            return Falsity()

        def next_op(operand):
            return Next(operand)

        def finally_op(operand):
            return Finally(operand)

        def globally_op(operand):
            return Globally(operand)

        def until_op(left, right):
            return Until(left, right)

        def release_op(left, right):
            return Release(left, right)

        local_vars = {
            'Variable': variable,
            'Not': not_op,
            'And': and_op,
            'Or': or_op,
            'Implication': implication,
            'Biconditional': biconditional,
            'Truth': truth,
            'Falsity': falsity,
            'Next': next_op,
            'Finally': finally_op,
            'Globally': globally_op,
            'Until': until_op,
            'Release': release_op
        }

        return eval(expr, {"__builtins__": None}, local_vars)


    return safe_eval(expression)