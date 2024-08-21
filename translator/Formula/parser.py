"""
This module provides functionality to parse logical formulae from string expressions.
It supports various logical operators and temporal logic operators.
"""



from .structure import Variable, Not, And, Or, Implication, Biconditional, Truth, Falsity, Next, Finally, Globally, Until, Release


def parse_formula(expression):
    """
    Parse a string expression into a Formula object.

    @param expression: A string representing a logical formula
    @return: A Formula object representing the parsed expression
    """


    def parse_expression(expression):
        """
        Recursively parse a string expression into a Formula object.

        @param expression: A string representing a logical formula or subformula
        @return: A Formula object representing the parsed expression
        """

        expression = expression.strip()
        if expression.startswith('(') and expression.endswith(')'):
            expression = expression[1:-1].strip()
        
        # Handle LTL operators
        for op, cls in [('X', Next), ('F', Finally), ('G', Globally)]:
            if expression.startswith(op):
                return cls(parse_expression(expression[1:].strip()))
        
        # Handle 'Until' and 'Release' operators
        for op, cls in [('U', Until), ('R', Release)]:
            parts = split_expression(expression, op)
            if len(parts) == 2:
                left, right = parts
                return cls(parse_expression(left), parse_expression(right))
        
        # Handle biconditional first
        for op, cls in [('<->', Biconditional)]:
            parts = split_expression(expression, op)
            if len(parts) == 2:
                left, right = parts
                return cls(parse_expression(left), parse_expression(right))
        
        # Handle implication
        for op, cls in [('->', Implication)]:
            parts = split_expression(expression, op)
            if len(parts) == 2:
                left, right = parts
                return cls(parse_expression(left), parse_expression(right))
        
        # Handle conjunction and disjunction
        for op, cls in [('&', And), ('|', Or)]:
            parts = split_expression(expression, op)
            if len(parts) == 2:
                left, right = parts
                return cls(parse_expression(left), parse_expression(right))
        
        # Handle 'Not' operator
        if expression.startswith('!'):
            return Not(parse_expression(expression[1:].strip()))
        
        # Handle variables and constants
        if expression in {'1', '0'}:
            return Truth() if expression == '1' else Falsity()
        
        return Variable(expression)
    
    
    def split_expression(expression, op):
        """
        Split an expression by a given operator, respecting parentheses.

        @param expression: The expression to split
        @param op: The operator to split on
        @return: A list of subexpressions
        """
        
        level = 0
        split_index = -1
        op_length = len(op)

        for i in range(len(expression)):
            if expression[i] == '(':
                level += 1
            elif expression[i] == ')':
                level -= 1
            elif level == 0 and expression[i:i+op_length] == op:
                split_index = i
                break

        if split_index == -1:
            return [expression]
        
        left = expression[:split_index].strip()
        right = expression[split_index + op_length:].strip()
        return [left, right]
    
    
    return parse_expression(expression)