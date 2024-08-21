"""
This module defines classes for representing and manipulating logical formulas. 
It includes an enumeration for different logical operations and various classes 
for each type of logical formula (e.g., AND, OR, NOT). Each class can generate 
string and representation forms of the formula, as well as identify its operation type.
"""



from enum import Enum, auto


class Operation(Enum):
    """
    Enumeration for logical operations. Each operation corresponds to a specific 
    logical operator used in formulas.
    """

    VARIABLE = auto()
    NOT = auto()
    AND = auto()
    OR = auto()
    IMPLICATION = auto()
    BICONDITIONAL = auto()
    TRUE = auto()
    FALSE = auto()
    NEXT = auto()
    FINALLY = auto()
    GLOBALLY = auto()
    UNTIL = auto()
    RELEASE = auto()


class Formula:
    """
    Base class for all logical formulas. Provides methods to generate string 
    and representation forms of formulas. Subclasses should override the _str 
    and _repr methods to provide specific behavior.
    """

    def __str__(self):
        pass

    def __str__(self):
        return self._str()

    def _str(self, parent_code=0):
        pass

    # Repr is (throughout this code) for testing purposes - to print an intermediary representation of a formula as it is within the code
    def __repr__(self):
        return self._repr()

    def _repr(self):
        return "<Formula>"


class Variable(Formula):
    """
    Class representing a logical variable in a formula.
    """

    def __init__(self, name):
        self.name = name

    def _str(self, parent_code=0):
        return self.name

    def code(self):
        return Operation.VARIABLE
    
    def __repr__(self):
        return f"Variable('{self.name}')"


class Truth(Formula):
    """
    Class representing a truth value (True) in a formula.
    """

    def _str(self, parent_code=0):
        return '1'

    def code(self):
        return Operation.TRUE
    
    def _repr(self):
        return "Truth()"


class Falsity(Formula):
    """
    Class representing a falsity value (False) in a formula.
    """

    def _str(self, parent_code=0):
        return '0'

    def code(self):
        return Operation.FALSE
    
    def _repr(self):
        return "Falsity()"


class Not(Formula):
    """
    Class representing a negation operation in a formula.
    """

    def __init__(self, operand):
        self.operand = operand

    def _str(self, parent_code=0):
        return f'!{self.operand}'

    def code(self):
        return Operation.NOT
    
    def _repr(self):
        return f"Not({repr(self.operand)})"


class And(Formula):
    """
    Class representing a logical AND operation in a formula.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def _str(self, parent_code=0):
        left_str = self.left._str(self.code())
        right_str = self.right._str(self.code())
        
        if (parent_code == Operation.OR or parent_code == Operation.NOT or parent_code == 0):
            return f'({left_str} & {right_str})'
        else:
            return f'{left_str} & {right_str}'

    def code(self):
        return Operation.AND
    
    def _repr(self):
        return f"And({repr(self.left)}, {repr(self.right)})"


class Or(Formula):
    """
    Class representing a logical OR operation in a formula.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def _str(self, parent_code=0):
        left_str = self.left._str(self.code())
        right_str = self.right._str(self.code())

        if (parent_code == Operation.AND or parent_code == Operation.NOT or parent_code == 0):
            return f'({left_str} | {right_str})'
        else:
            return f'{left_str} | {right_str}'

    def code(self):
        return Operation.OR
    
    def _repr(self):
        return f"Or({repr(self.left)}, {repr(self.right)})"


class Implication(Formula):
    """
    Class representing a logical implication (->) in a formula.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def _str(self, parent_code=0):
        left_str = self.left._str(self.code())
        right_str = self.right._str(self.code())

        return f'({left_str} -> {right_str})'

    def code(self):
        return Operation.IMPLICATION
    
    def _repr(self):
        return f"Implication({repr(self.left)}, {repr(self.right)})"


class Biconditional(Formula):
    """
    Class representing a logical biconditional (<->) in a formula.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def _str(self, parent_code=0):
        left_str = self.left._str(self.code())
        right_str = self.right._str(self.code())

        return f'({left_str} <-> {right_str})'

    def code(self):
        return Operation.BICONDITIONAL
    
    def _repr(self):
        return f"Biconditional({repr(self.left)}, {repr(self.right)})"


class Next(Formula):
    """
    Class representing the temporal 'Next' (X) operator in a formula.
    """

    def __init__(self, operand):
        self.operand = operand

    def _str(self, parent_code=0):
        return f'X {self.operand}'

    def code(self):
        return Operation.NEXT
    
    def _repr(self):
        return f"Next({repr(self.operand)})"


class Finally(Formula):
    """
    Class representing the temporal 'Finally' (F) operator in a formula.
    """

    def __init__(self, operand):
        self.operand = operand

    def _str(self, parent_code=0):
        return f'F {self.operand}'

    def code(self):
        return Operation.FINALLY

    def _repr(self):
        return f"Finally({repr(self.operand)})"


class Globally(Formula):
    """
    Class representing the temporal 'Globally' (G) operator in a formula.
    """
     
    def __init__(self, operand):
        self.operand = operand

    def _str(self, parent_code=0):
        return f'G {self.operand}'

    def code(self):
        return Operation.GLOBALLY

    def _repr(self):
        return f"Globally({repr(self.operand)})"


class Until(Formula):
    """
    Class representing the temporal 'Until' (U) operator in a formula.
    """

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def _str(self, parent_code=0):
        left_str = self.left._str(self.code())
        right_str = self.right._str(self.code())
        return f'({left_str} U {right_str})'

    def code(self):
        return Operation.UNTIL
    
    def _repr(self):
        return f"Until({repr(self.left)}, {repr(self.right)})"


class Release(Formula):
    """
    Class representing the temporal 'Release' (R) operator in a formula.
    """
    
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def _str(self, parent_code=0):
        left_str = self.left._str(self.code())
        right_str = self.right._str(self.code())
        return f'({left_str} R {right_str})'

    def code(self):
        return Operation.RELEASE
    
    def _repr(self):
        return f"Release({repr(self.left)}, {repr(self.right)})"