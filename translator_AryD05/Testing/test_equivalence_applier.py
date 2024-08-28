from ..Equivalence_Applier.applier import apply_equivalences


def test_equivalence_applier(formula_str: str):
    equivalents = apply_equivalences(formula_str, 2.5, 3)

    print("Testing equivalence applier:")
    print("Original Formula:")
    print(formula_str)
    
    print("\nEquivalent Formulae:")
    for eq in equivalents:
        print(eq._str())