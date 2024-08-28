from ..Formula.structure import Formula, Variable, And, Or, Not, Implication, Biconditional, Truth, Falsity, Next, Finally, Globally, Until, Release
from ..Equivalence_Applier.equivalences import *  # Import all equivalences


def test_equivalences():
    a = Variable('a')
    b = Variable('b')
    c = Variable('c')

    tests = [
        (implication_to_disjunction, Implication(a, b), Or(Not(a), b)),
        (biconditional_to_implications, Biconditional(a, b), And(Implication(a, b), Implication(b, a))),
        (double_negation, Not(Not(a)), a),
        (de_morgan_not_and, Not(And(a, b)), Or(Not(a), Not(b))),
        (de_morgan_not_or, Not(Or(a, b)), And(Not(a), Not(b))),
        (distributive_law_and_or, And(a, Or(b, c)), Or(And(a, b), And(a, c))),
        (commutativity_and, And(a, b), And(b, a)),
        (commutativity_or, Or(a, b), Or(b, a)),
        (associativity_and, And(And(a, b), c), And(a, And(b, c))),
        (associativity_or, Or(Or(a, b), c), Or(a, Or(b, c))),
        (absorption_and, And(a, Or(a, b)), a),
        (absorption_or, Or(a, And(a, b)), a),
        (idempotence_and, And(a, a), a),
        (idempotence_or, Or(a, a), a),
        (and_truth, And(a, Truth()), a),
        (or_truth, Or(a, Truth()), Truth()),
        (and_falsity, And(a, Falsity()), Falsity()),
        (or_falsity, Or(a, Falsity()), a),
        (not_truth, Not(Truth()), Falsity()),
        (not_falsity, Not(Falsity()), Truth()),
        (law_of_excluded_middle, Or(a, Not(a)), Truth()),
        (non_contradiction_to_falsity, And(a, Not(a)), Falsity()),
        (distribute_next_over_and, Next(And(a, b)), And(Next(a), Next(b))),
        (distribute_next_over_or, Next(Or(a, b)), Or(Next(a), Next(b))),
        (distribute_next_over_until, Next(Until(a, b)), Until(Next(a), Next(b))),
        (distribute_finally_over_or, Finally(Or(a, b)), Or(Finally(a), Finally(b))),
        (distribute_globally_over_and, Globally(And(a, b)), And(Globally(a), Globally(b))),
        (distribute_until_over_or, Until(Or(a, b), c), Or(Until(a, c), Until(b, c))),
        (distribute_and_over_until, And(Until(a, b), Until(a, c)), Until(a, And(b, c))),
        (negate_next, Not(Next(a)), Next(Not(a))),
        (negate_finally, Not(Finally(a)), Globally(Not(a))),
        (negate_until, Not(Until(a, b)), Release(Not(a), Not(b))),
        (negate_globally, Not(Globally(a)), Finally(Not(a))),
        (negate_release, Not(Release(a, b)), Until(Not(a), Not(b))),
        (finally_idempotence, Finally(Finally(a)), Finally(a)),
        (globally_idempotence, Globally(Globally(a)), Globally(a)),
        (until_idempotence, Until(a, Until(a, b)), Until(a, b)),
        (until_expansion, Until(a, b), Or(b, And(a, Next(Until(a, b))))),
        (release_expansion, Release(a, b), And(b, Or(a, Next(Release(a, b))))),
        (globally_expansion, Globally(a), And(a, Next(Globally(a)))),
        (finally_expansion, Finally(a), Or(a, Next(Finally(a)))),
        (finally_to_until, Finally(a), Until(Truth(), a)),
        (globally_to_release, Globally(a), Release(Falsity(), a)),
        (reverse_implication_to_disjunction, Or(Not(a), b), Implication(a, b)),
        (reverse_biconditional_to_implications, And(Implication(a, b), Implication(b, a)), Biconditional(a, b)),
        (reverse_double_negation, a, Not(Not(a))),
        (reverse_de_morgan_not_and, Or(Not(a), Not(b)), Not(And(a, b))),
        (reverse_de_morgan_not_or, And(Not(a), Not(b)), Not(Or(a, b))),
        (reverse_distributive_law_and_or, Or(And(a, b), And(a, c)), And(a, Or(b, c))),
        (reverse_commutativity_and, And(b, a), And(a, b)),
        (reverse_commutativity_or, Or(b, a), Or(a, b)),
        (reverse_associativity_and, And(a, And(b, c)), And(And(a, b), c)),
        (reverse_associativity_or, Or(a, Or(b, c)), Or(Or(a, b), c)),
        (reverse_idempotence_and, a, And(a, a)),
        (reverse_idempotence_or, a, Or(a, a)),
        (reverse_and_truth, a, And(a, Truth())),
        (reverse_or_falsity, a, Or(a, Falsity())),
        (reverse_not_truth, Falsity(), Not(Truth())),
        (reverse_not_falsity, Truth(), Not(Falsity())),
        (reverse_distribute_next_over_and, And(Next(a), Next(b)), Next(And(a, b))),
        (reverse_distribute_next_over_or, Or(Next(a), Next(b)), Next(Or(a, b))),
        (reverse_distribute_next_over_until, Until(Next(a), Next(b)), Next(Until(a, b))),
        (reverse_distribute_finally_over_or, Or(Finally(a), Finally(b)), Finally(Or(a, b))),
        (reverse_distribute_globally_over_and, And(Globally(a), Globally(b)), Globally(And(a, b))),
        (reverse_distribute_until_over_or, Or(Until(a, c), Until(b, c)), Until(Or(a, b), c)),
        (reverse_distribute_and_over_until, Until(a, And(b, c)), And(Until(a, b), Until(a, c))),
        (reverse_negate_next, Next(Not(a)), Not(Next(a))),
        (reverse_negate_finally, Globally(Not(a)), Not(Finally(a))),
        (reverse_negate_until, Release(Not(a), Not(b)), Not(Until(a, b))),
        (reverse_negate_globally, Finally(Not(a)), Not(Globally(a))),
        (reverse_negate_release, Until(Not(a), Not(b)), Not(Release(a, b))),
        (reverse_finally_idempotence, Finally(a), Finally(Finally(a))),
        (reverse_globally_idempotence, Globally(a), Globally(Globally(a))),
        (reverse_until_idempotence, Until(a, b), Until(a, Until(a, b))),
        (reverse_until_expansion, Or(b, And(a, Next(Until(a, b)))), Until(a, b)),
        (reverse_release_expansion, And(b, Or(a, Next(Release(a, b)))), Release(a, b)),
        (reverse_globally_expansion, And(a, Next(Globally(a))), Globally(a)),
        (reverse_finally_expansion, Or(a, Next(Finally(a))), Finally(a)),
        (reverse_finally_to_until, Until(Truth(), a), Finally(a)),
        (reverse_globally_to_release, Release(Falsity(), a), Globally(a)),
        (implication_to_true, Implication(a, a), Truth()),
        (false_implies_anything, Implication(Falsity(), a), Truth()),
        (implication_to_negation, Implication(a, b), Or(Not(a), b)),
        (reverse_implication_to_negation, Or(Not(a), b), Implication(a, b)),
        (xor_equivalence, Or(And(a, Not(b)), And(Not(a), b)), Not(Biconditional(a, b))),
        (reverse_xor_equivalence, Not(Biconditional(a, b)), Or(And(a, Not(b)), And(Not(a), b))),
    ]

    passed = 0
    failed = 0

    for equivalence, input_formula, expected_output in tests:
        result = equivalence(input_formula)
        if str(result) == str(expected_output):
            print(f"PASS: {equivalence.__name__}")
            passed += 1
        else:
            print(f"FAIL: {equivalence.__name__}")
            print(f"  Expected: {expected_output}")
            print(f"  Got: {result}")
            failed += 1

    print(f"\nTotal tests: {passed + failed}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    return passed, failed