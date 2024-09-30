'''
This module defines logical equivalences for formula transformations.
It includes a set of equivalence functions and a tuple of all available equivalences.
'''



from Formula.structure import Formula, Variable, Not, And, Or, Implication, Biconditional, Truth, Falsity, Next, Globally, Finally, Until, Release
from typing import Tuple, Callable


# Define a type for equivalence functions
EquivalenceFunction = Callable[[Formula], Formula]


# Define the equivalences
def implication_to_disjunction(formula: Formula) -> Formula:
    if isinstance(formula, Implication):
        return Or(Not(formula.left), formula.right)
    return formula

def biconditional_to_implications(formula: Formula) -> Formula:
    if isinstance(formula, Biconditional):
        return And(Implication(formula.left, formula.right), Implication(formula.right, formula.left))
    return formula

def double_negation(formula: Formula) -> Formula:
    if isinstance(formula, Not) and isinstance(formula.operand, Not):
        return formula.operand.operand
    return formula

def de_morgan_not_and(formula: Formula) -> Formula:
    if isinstance(formula, Not) and isinstance(formula.operand, And):
        return Or(Not(formula.operand.left), Not(formula.operand.right))
    return formula

def de_morgan_not_or(formula: Formula) -> Formula:
    if isinstance(formula, Not) and isinstance(formula.operand, Or):
        return And(Not(formula.operand.left), Not(formula.operand.right))
    return formula

def distributive_law_and_or(formula: Formula) -> Formula:
    if isinstance(formula, And) and isinstance(formula.right, Or):
        return Or(And(formula.left, formula.right.left), And(formula.left, formula.right.right))
    if isinstance(formula, Or) and isinstance(formula.right, And):
        return And(Or(formula.left, formula.right.left), Or(formula.left, formula.right.right))
    return formula

def commutativity_and(formula: Formula) -> Formula:
    if isinstance(formula, And):
        return And(formula.right, formula.left)
    return formula

def commutativity_or(formula: Formula) -> Formula:
    if isinstance(formula, Or):
        return Or(formula.right, formula.left)
    return formula

def associativity_and(formula: Formula) -> Formula:
    if isinstance(formula, And) and isinstance(formula.right, And):
        return And(And(formula.left, formula.right.left), formula.right.right)
    return formula

def associativity_or(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.right, Or):
        return Or(Or(formula.left, formula.right.left), formula.right.right)
    return formula

def absorption_and(formula: Formula) -> Formula:
    if isinstance(formula, And) and isinstance(formula.right, Or):
        if formula.left == formula.right.left:
            return formula.left
    return formula

def absorption_or(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.right, And):
        if formula.left == formula.right.left:
            return formula.left
    return formula

def idempotence_and(formula: Formula) -> Formula:
    if isinstance(formula, And) and formula.left == formula.right:
        return formula.left
    return formula

def idempotence_or(formula: Formula) -> Formula:
    if isinstance(formula, Or) and formula.left == formula.right:
        return formula.left
    return formula

def and_truth(formula: Formula) -> Formula:
    if isinstance(formula, And):
        if isinstance(formula.left, Truth):
            return formula.right
        if isinstance(formula.right, Truth):
            return formula.left
    return formula

def or_truth(formula: Formula) -> Formula:
    if isinstance(formula, Or):
        if isinstance(formula.left, Truth) or isinstance(formula.right, Truth):
            return Truth()
    return formula

def and_falsity(formula: Formula) -> Formula:
    if isinstance(formula, And):
        if isinstance(formula.left, Falsity) or isinstance(formula.right, Falsity):
            return Falsity()
    return formula

def or_falsity(formula: Formula) -> Formula:
    if isinstance(formula, Or):
        if isinstance(formula.left, Falsity):
            return formula.right
        if isinstance(formula.right, Falsity):
            return formula.left
    return formula

def not_truth(formula: Formula) -> Formula:
    if isinstance(formula, Not) and isinstance(formula.operand, Truth):
        return Falsity()
    return formula

def not_falsity(formula: Formula) -> Formula:
    if isinstance(formula, Not) and isinstance(formula.operand, Falsity):
        return Truth()
    return formula

def law_of_excluded_middle(formula: Formula) -> Formula:
    if isinstance(formula, Or):
        left, right = formula.left, formula.right
        if isinstance(left, Variable) and isinstance(right, Not):
            if isinstance(right.operand, Variable) and right.operand.name == left.name:
                return Truth()
        
        if isinstance(right, Variable) and isinstance(left, Not):
            if isinstance(left.operand, Variable) and left.operand.name == right.name:
                return Truth()
    return formula

def non_contradiction_to_falsity(formula: Formula) -> Formula:
    if isinstance(formula, And):
        if isinstance(formula.left, Not) and formula.left.operand == formula.right:
            return Falsity()
        if isinstance(formula.right, Not) and formula.right.operand == formula.left:
            return Falsity()
    return formula

def distribute_next_over_and(formula: Formula) -> Formula:
    if isinstance(formula, Next) and isinstance(formula.operand, And):
        return And(Next(formula.operand.left), Next(formula.operand.right))
    return formula

def distribute_next_over_or(formula: Formula) -> Formula:
    if isinstance(formula, Next) and isinstance(formula.operand, Or):
        return Or(Next(formula.operand.left), Next(formula.operand.right))
    return formula

def distribute_next_over_until(formula: Formula) -> Formula:
    if isinstance(formula, Next) and isinstance(formula.operand, Until):
        return Until(Next(formula.operand.left), Next(formula.operand.right))
    return formula

def distribute_finally_over_or(formula: Formula) -> Formula:
    if isinstance(formula, Finally) and isinstance(formula.operand, Or):
        return Or(Finally(formula.operand.left), Finally(formula.operand.right))
    return formula

def distribute_globally_over_and(formula: Formula) -> Formula:
    if isinstance(formula, Globally) and isinstance(formula.operand, And):
        return And(Globally(formula.operand.left), Globally(formula.operand.right))
    return formula

def distribute_until_over_or(formula: Formula) -> Formula:
    if isinstance(formula, Until) and isinstance(formula.left, Or):
        return Or(Until(formula.left.left, formula.right), Until(formula.left.right, formula.right))
    return formula

def distribute_and_over_until(formula: Formula) -> Formula:
    if isinstance(formula, And) and isinstance(formula.left, Until) and isinstance(formula.right, Until):
        if formula.left.left == formula.right.left:
            return Until(formula.left.left, And(formula.left.right, formula.right.right))
    return formula

def negate_next(formula: Formula) -> Formula:
    if isinstance(formula, Not) and isinstance(formula.operand, Next):
        return Next(Not(formula.operand.operand))
    return formula

def negate_finally(formula: Formula) -> Formula:
    if isinstance(formula, Not) and isinstance(formula.operand, Finally):
        return Globally(Not(formula.operand.operand))
    return formula

def negate_until(formula: Formula) -> Formula:
    if isinstance(formula, Not) and isinstance(formula.operand, Until):
        return Release(Not(formula.operand.left), Not(formula.operand.right))
    return formula

def negate_globally(formula: Formula) -> Formula:
    if isinstance(formula, Not) and isinstance(formula.operand, Globally):
        return Finally(Not(formula.operand.operand))
    return formula

def negate_release(formula: Formula) -> Formula:
    if isinstance(formula, Not) and isinstance(formula.operand, Release):
        return Until(Not(formula.operand.left), Not(formula.operand.right))
    return formula

def finally_idempotence(formula: Formula) -> Formula:
    if isinstance(formula, Finally) and isinstance(formula.operand, Finally):
        return Finally(formula.operand.operand)
    return formula

def globally_idempotence(formula: Formula) -> Formula:
    if isinstance(formula, Globally) and isinstance(formula.operand, Globally):
        return Globally(formula.operand.operand)
    return formula

def until_idempotence(formula: Formula) -> Formula:
    if isinstance(formula, Until) and isinstance(formula.right, Until) and formula.left == formula.right.left:
        return Until(formula.left, formula.right.right)
    return formula

def until_expansion(formula: Formula) -> Formula:
    if isinstance(formula, Until):
        return Or(formula.right, And(formula.left, Next(formula)))
    return formula

def release_expansion(formula: Formula) -> Formula:
    if isinstance(formula, Release):
        return And(formula.right, Or(formula.left, Next(formula)))
    return formula

def globally_expansion(formula: Formula) -> Formula:
    if isinstance(formula, Globally):
        return And(formula.operand, Next(formula))
    return formula

def finally_expansion(formula: Formula) -> Formula:
    if isinstance(formula, Finally):
        return Or(formula.operand, Next(formula))
    return formula

def finally_to_until(formula: Formula) -> Formula:
    if isinstance(formula, Finally):
        return Until(Truth(), formula.operand)
    return formula

def globally_to_release(formula: Formula) -> Formula:
    if isinstance(formula, Globally):
        return Release(Falsity(), formula.operand)
    return formula

def reverse_implication_to_disjunction(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.left, Not):
        return Implication(formula.left.operand, formula.right)
    return formula

def reverse_biconditional_to_implications(formula: Formula) -> Formula:
    if isinstance(formula, And) and isinstance(formula.left, Implication) and isinstance(formula.right, Implication):
        if formula.left.left == formula.right.right and formula.left.right == formula.right.left:
            return Biconditional(formula.left.left, formula.left.right)
    return formula

def reverse_double_negation(formula: Formula) -> Formula:
    if not isinstance(formula, (And, Or, Implication, Biconditional, Next, Finally, Globally, Until, Release)):
        return Not(Not(formula))
    return formula

def reverse_de_morgan_not_and(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.left, Not) and isinstance(formula.right, Not):
        return Not(And(formula.left.operand, formula.right.operand))
    return formula

def reverse_de_morgan_not_or(formula: Formula) -> Formula:
    if isinstance(formula, And) and isinstance(formula.left, Not) and isinstance(formula.right, Not):
        return Not(Or(formula.left.operand, formula.right.operand))
    return formula

def reverse_distributive_law_and_or(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.left, And) and isinstance(formula.right, And):
        if formula.left.left == formula.right.left:
            return And(formula.left.left, Or(formula.left.right, formula.right.right))
    return formula

def reverse_commutativity_and(formula: Formula) -> Formula:
    if isinstance(formula, And):
        return And(formula.right, formula.left)
    return formula

def reverse_commutativity_or(formula: Formula) -> Formula:
    if isinstance(formula, Or):
        return Or(formula.right, formula.left)
    return formula

def reverse_associativity_and(formula: Formula) -> Formula:
    if isinstance(formula, And) and isinstance(formula.left, And):
        return And(formula.left.left, And(formula.left.right, formula.right))
    return formula

def reverse_associativity_or(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.left, Or):
        return Or(formula.left.left, Or(formula.left.right, formula.right))
    return formula

def reverse_idempotence_and(formula: Formula) -> Formula:
    if not isinstance(formula, (And, Or, Implication, Biconditional, Next, Finally, Globally, Until, Release)):
        return And(formula, formula)
    return formula

def reverse_idempotence_or(formula: Formula) -> Formula:
    if not isinstance(formula, (And, Or, Implication, Biconditional, Next, Finally, Globally, Until, Release)):
        return Or(formula, formula)
    return formula

def reverse_and_truth(formula: Formula) -> Formula:
    if not isinstance(formula, (And, Or, Implication, Biconditional, Next, Finally, Globally, Until, Release)):
        return And(formula, Truth())
    return formula

def reverse_or_falsity(formula: Formula) -> Formula:
    if not isinstance(formula, (And, Or, Implication, Biconditional, Next, Finally, Globally, Until, Release)):
        return Or(formula, Falsity())
    return formula

def reverse_not_truth(formula: Formula) -> Formula:
    if isinstance(formula, Falsity):
        return Not(Truth())
    return formula

def reverse_not_falsity(formula: Formula) -> Formula:
    if isinstance(formula, Truth):
        return Not(Falsity())
    return formula

def reverse_distribute_next_over_and(formula: Formula) -> Formula:
    if isinstance(formula, And) and isinstance(formula.left, Next) and isinstance(formula.right, Next):
        return Next(And(formula.left.operand, formula.right.operand))
    return formula

def reverse_distribute_next_over_or(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.left, Next) and isinstance(formula.right, Next):
        return Next(Or(formula.left.operand, formula.right.operand))
    return formula

def reverse_distribute_next_over_until(formula: Formula) -> Formula:
    if isinstance(formula, Until) and isinstance(formula.left, Next) and isinstance(formula.right, Next):
        return Next(Until(formula.left.operand, formula.right.operand))
    return formula

def reverse_distribute_finally_over_or(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.left, Finally) and isinstance(formula.right, Finally):
        return Finally(Or(formula.left.operand, formula.right.operand))
    return formula

def reverse_distribute_globally_over_and(formula: Formula) -> Formula:
    if isinstance(formula, And) and isinstance(formula.left, Globally) and isinstance(formula.right, Globally):
        return Globally(And(formula.left.operand, formula.right.operand))
    return formula

def reverse_distribute_until_over_or(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.left, Until) and isinstance(formula.right, Until):
        if formula.left.right == formula.right.right:
            return Until(Or(formula.left.left, formula.right.left), formula.left.right)
    return formula

def reverse_distribute_and_over_until(formula: Formula) -> Formula:
    if isinstance(formula, Until) and isinstance(formula.right, And):
        return And(Until(formula.left, formula.right.left), Until(formula.left, formula.right.right))
    return formula

def reverse_negate_next(formula: Formula) -> Formula:
    if isinstance(formula, Next) and isinstance(formula.operand, Not):
        return Not(Next(formula.operand.operand))
    return formula

def reverse_negate_finally(formula: Formula) -> Formula:
    if isinstance(formula, Globally) and isinstance(formula.operand, Not):
        return Not(Finally(formula.operand.operand))
    return formula

def reverse_negate_until(formula: Formula) -> Formula:
    if isinstance(formula, Release) and isinstance(formula.left, Not) and isinstance(formula.right, Not):
        return Not(Until(formula.left.operand, formula.right.operand))
    return formula

def reverse_negate_globally(formula: Formula) -> Formula:
    if isinstance(formula, Finally) and isinstance(formula.operand, Not):
        return Not(Globally(formula.operand.operand))
    return formula

def reverse_negate_release(formula: Formula) -> Formula:
    if isinstance(formula, Until) and isinstance(formula.left, Not) and isinstance(formula.right, Not):
        return Not(Release(formula.left.operand, formula.right.operand))
    return formula

def reverse_finally_idempotence(formula: Formula) -> Formula:
    if isinstance(formula, Finally):
        return Finally(Finally(formula.operand))
    return formula

def reverse_globally_idempotence(formula: Formula) -> Formula:
    if isinstance(formula, Globally):
        return Globally(Globally(formula.operand))
    return formula

def reverse_until_idempotence(formula: Formula) -> Formula:
    if isinstance(formula, Until):
        return Until(formula.left, Until(formula.left, formula.right))
    return formula

def reverse_until_expansion(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.right, And) and isinstance(formula.right.right, Next):
        if isinstance(formula.right.right.operand, Until) and formula.right.left == formula.right.right.operand.left:
            return formula.right.right.operand
    return formula

def reverse_release_expansion(formula: Formula) -> Formula:
    if isinstance(formula, And) and isinstance(formula.right, Or) and isinstance(formula.right.right, Next):
        if isinstance(formula.right.right.operand, Release) and formula.right.left == formula.right.right.operand.left:
            return formula.right.right.operand
    return formula

def reverse_globally_expansion(formula: Formula) -> Formula:
    if isinstance(formula, And) and isinstance(formula.right, Next):
        if isinstance(formula.right.operand, Globally) and formula.left == formula.right.operand.operand:
            return formula.right.operand
    return formula

def reverse_finally_expansion(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.right, Next):
        if isinstance(formula.right.operand, Finally) and formula.left == formula.right.operand.operand:
            return formula.right.operand
    return formula

def reverse_finally_to_until(formula: Formula) -> Formula:
    if isinstance(formula, Until) and isinstance(formula.left, Truth):
        return Finally(formula.right)
    return formula

def reverse_globally_to_release(formula: Formula) -> Formula:
    if isinstance(formula, Release) and isinstance(formula.left, Falsity):
        return Globally(formula.right)
    return formula

def implication_to_true(formula: Formula) -> Formula:
    if isinstance(formula, Implication) and formula.left == formula.right:
        return Truth()
    return formula

def false_implies_anything(formula: Formula) -> Formula:
    if isinstance(formula, Implication):
        if isinstance(formula.left, Falsity):
            return Truth()
    return formula

def implication_to_negation(formula: Formula) -> Formula:
    if isinstance(formula, Implication):
        return Or(Not(formula.left), formula.right)
    return formula

def reverse_implication_to_negation(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.left, Not):
        return Implication(formula.left.operand, formula.right)
    return formula

def xor_equivalence(formula: Formula) -> Formula:
    if isinstance(formula, Or) and isinstance(formula.left, And) and isinstance(formula.right, And):
        a = formula.left.left
        b = formula.right.right
        if (isinstance(formula.left.right, Not) and 
            isinstance(formula.right.left, Not) and
            formula.left.right.operand == b and
            formula.right.left.operand == a):
            return Not(Biconditional(a, b))
    return formula

def reverse_xor_equivalence(formula: Formula) -> Formula:
    if isinstance(formula, Not) and isinstance(formula.operand, Biconditional):
        a, b = formula.operand.left, formula.operand.right
        return Or(And(a, Not(b)), And(Not(a), b))
    return formula


# List of equivalences
EQUIVALENCES: Tuple[EquivalenceFunction] = (
    implication_to_disjunction,
    biconditional_to_implications,
    double_negation,
    de_morgan_not_and,
    de_morgan_not_or,
    distributive_law_and_or,
    commutativity_and,
    commutativity_or,
    associativity_and,
    associativity_or,
    absorption_and,
    absorption_or,
    idempotence_and,
    idempotence_or,
    and_truth,
    or_truth,
    and_falsity,
    or_falsity,
    not_truth,
    not_falsity,
    law_of_excluded_middle,
    non_contradiction_to_falsity,
    distribute_next_over_and,
    distribute_next_over_or,
    distribute_next_over_until,
    distribute_finally_over_or,
    distribute_globally_over_and,
    distribute_until_over_or,
    distribute_and_over_until,
    negate_next,
    negate_finally,
    negate_until,
    negate_globally,
    negate_release,
    finally_idempotence,
    globally_idempotence,
    until_idempotence,
    until_expansion,
    release_expansion,
    globally_expansion,
    finally_expansion,
    finally_to_until,
    globally_to_release,
    reverse_implication_to_disjunction,
    reverse_biconditional_to_implications,
    reverse_double_negation,
    reverse_de_morgan_not_and,
    reverse_de_morgan_not_or,
    reverse_distributive_law_and_or,
    reverse_commutativity_and,
    reverse_commutativity_or,
    reverse_associativity_and,
    reverse_associativity_or,
    reverse_idempotence_and,
    reverse_idempotence_or,
    reverse_and_truth,
    reverse_or_falsity,
    reverse_not_truth,
    reverse_not_falsity,
    reverse_distribute_next_over_and,
    reverse_distribute_next_over_or,
    reverse_distribute_next_over_until,
    reverse_distribute_finally_over_or,
    reverse_distribute_globally_over_and,
    reverse_distribute_until_over_or,
    reverse_distribute_and_over_until,
    reverse_negate_next,
    reverse_negate_finally,
    reverse_negate_until,
    reverse_negate_globally,
    reverse_negate_release,
    reverse_finally_idempotence,
    reverse_globally_idempotence,
    reverse_until_idempotence,
    reverse_until_expansion,
    reverse_release_expansion,
    reverse_globally_expansion,
    reverse_finally_expansion,
    reverse_finally_to_until,
    reverse_globally_to_release,
    implication_to_true,
    false_implies_anything,
    implication_to_negation,
    reverse_implication_to_negation,
    xor_equivalence,
    reverse_xor_equivalence
    # Add more equivalences here if needed
)