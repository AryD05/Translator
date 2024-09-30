'''
This module contains functions for applying equivalences to logical formulae.
It uses a complexity-based approach to generate equivalent formulae within specified constraints.
'''



from Formula.structure import Formula, And, Or, Not, Implication, Biconditional, Variable, Truth, Falsity, Next, Finally, Globally, Until, Release
from Formula.parser import parse_formula
from .equivalences import EQUIVALENCES
from typing import List, Callable, Tuple


def formula_complexity(formula: Formula) -> int:
    '''
    Calculate the complexity of a given formula.

    @param formula: The formula to calculate complexity for
    @return: An integer representing the formula's complexity
    '''

    if isinstance(formula, (Variable, Truth, Falsity)):
        return 1
    elif isinstance(formula, (Not, Next, Finally, Globally)):
        return 1 + formula_complexity(formula.operand)
    elif isinstance(formula, (And, Or, Implication, Biconditional, Until, Release)):
        return 1 + formula_complexity(formula.left) + formula_complexity(formula.right)
    return 1


def apply_equivalences_to_subformulae(formula: Formula, equivalences: Tuple[Callable[[Formula], Formula]], max_depth: int, depth: int = 0) -> List[Formula]:
    '''
    Apply equivalences to subformulae of the given formula up to a maximum depth.

    @param formula: The formula to apply equivalences to
    @param equivalences: A tuple of equivalence functions to apply
    @param max_depth: The maximum depth to apply equivalences
    @param depth: The current depth in the recursion
    @return: A list of equivalent formulae
    '''
    
    if depth > max_depth:
        return [formula]

    results = [formula]  # Start with the original formula
    
    # Apply equivalences at the current level
    for equivalence in equivalences:
        new_formula = equivalence(formula)
        if str(new_formula) != str(formula):
            results.append(new_formula)

    # Apply equivalences to subformulae
    if isinstance(formula, (Not, Next, Finally, Globally)):
        sub_results = apply_equivalences_to_subformulae(formula.operand, equivalences, max_depth, depth + 1)
        results.extend([formula.__class__(sub) for sub in sub_results])
    elif isinstance(formula, (And, Or, Implication, Biconditional, Until, Release)):
        left_results = apply_equivalences_to_subformulae(formula.left, equivalences, max_depth, depth + 1)
        right_results = apply_equivalences_to_subformulae(formula.right, equivalences, max_depth, depth + 1)
        for left in left_results:
            for right in right_results:
                results.append(formula.__class__(left, right))

    return results


def apply_equivalences(formula_str: str, complexity_threshold: float, max_depth: int) -> List[Formula]:
    '''
    Apply equivalences to a formula string, generating equivalent formulae within complexity constraints.

    @param formula_str: The input formula as a string
    @param complexity_threshold: The maximum allowed complexity as a factor of the original formula's complexity
    @param max_depth: The maximum depth to apply equivalences
    @return: A list of equivalent formulae
    '''
    
    formula = parse_formula(formula_str)
    original_complexity = formula_complexity(formula)

    results = [formula]
    queue = [formula]
    seen = {str(formula)}

    while queue:
        current_formula = queue.pop(0)

        new_formulas = apply_equivalences_to_subformulae(current_formula, EQUIVALENCES, max_depth)
        
        for new_formula in new_formulas:
            new_complexity = formula_complexity(new_formula)
            
            if str(new_formula) not in seen and new_complexity <= original_complexity * complexity_threshold:
                results.append(new_formula)
                queue.append(new_formula)
                seen.add(str(new_formula))

    return results