'''
This module provides functionality to filter equivalences based on allowed operators.
It ensures that only formulae containing specified operators are included in the result.
'''



from typing import List, Set
from Formula.structure import Formula, Variable, Not, And, Or, Implication, Biconditional, Truth, Falsity, Next, Finally, Globally, Until, Release


def filter_equivalences(equivalences: List[Formula], allowed_operators: Set[str]) -> List[Formula]:
    '''
    Filter a list of equivalences based on allowed operators.

    @param equivalences: A list of formulae to filter
    @param allowed_operators: A set of allowed operator symbols
    @return: A list of formulae containing only allowed operators
    '''
    

    def is_allowed(formula: Formula) -> bool:
        if isinstance(formula, Variable):
            return True
        elif isinstance(formula, Truth) and '1' in allowed_operators:
            return True
        elif isinstance(formula, Falsity) and '0' in allowed_operators:
            return True
        elif isinstance(formula, Not) and '!' in allowed_operators:
            return is_allowed(formula.operand)
        elif isinstance(formula, And) and '&' in allowed_operators:
            return is_allowed(formula.left) and is_allowed(formula.right)
        elif isinstance(formula, Or) and '|' in allowed_operators:
            return is_allowed(formula.left) and is_allowed(formula.right)
        elif isinstance(formula, Implication) and '->' in allowed_operators:
            return is_allowed(formula.left) and is_allowed(formula.right)
        elif isinstance(formula, Biconditional) and '<->' in allowed_operators:
            return is_allowed(formula.left) and is_allowed(formula.right)
        elif isinstance(formula, Next) and 'X' in allowed_operators:
            return is_allowed(formula.operand)
        elif isinstance(formula, Finally) and 'F' in allowed_operators:
            return is_allowed(formula.operand)
        elif isinstance(formula, Globally) and 'G' in allowed_operators:
            return is_allowed(formula.operand)
        elif isinstance(formula, Until) and 'U' in allowed_operators:
            return is_allowed(formula.left) and is_allowed(formula.right)
        elif isinstance(formula, Release) and 'R' in allowed_operators:
            return is_allowed(formula.left) and is_allowed(formula.right)
        else:
            return False

    print(f"Filtering {len(equivalences)} equivalences with allowed operators: {allowed_operators}")


    filtered_equivalences = [eq for eq in equivalences if is_allowed(eq)]

    print(f"Filtered to {len(filtered_equivalences)} equivalences")

    return filtered_equivalences