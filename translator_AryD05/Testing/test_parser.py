from ..Formula.parser import parse_formula


def test_parser(formula_str: str):
    try:
        formula = parse_formula(formula_str)
        print("Testing parser:")
        print("Original formula string:", formula_str)
        print("Intermediate Formula Structure (default repr):")
        print(repr(formula))

    except Exception as e:
        print(f"An error occurred: {e}")