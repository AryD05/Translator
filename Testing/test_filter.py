from Equivalence_Applier.applier import apply_equivalences
from Equivalence_Applier.filter import filter_equivalences


def test_filter(formula_str: str):
    print("Original Formula:")
    print(formula_str)
    
    # Generate equivalences
    equivalents = apply_equivalences(formula_str, 2.5, 3)
    
    print(f"\nTotal number of equivalences generated: {len(equivalents)}")

    #Allowed operators
    allowed_operators = get_allowed_operators()
    
    # Filter equivalences
    filtered_equivalents = filter_equivalences(equivalents, allowed_operators)
    
    print(f"\nNumber of filtered equivalences: {len(filtered_equivalents)}")
    print("\nFiltered Equivalent Formulae:")
    for eq in filtered_equivalents:
        print(eq._str())


def get_allowed_operators() -> set[str]:
    print("Enter the allowed operators separated by commas.")
    print("Valid operators are: !, &, |, ->, <->")
    print("Atoms are allowed by default.")
    
    input_str = input("Allowed operators: ")
    allowed_operators = set(op.strip() for op in input_str.split(','))

    return allowed_operators