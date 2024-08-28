from ..Formula.structure import Variable, Not, And, Or, Implication, Truth, Falsity


def test_structure():
    try:
        formula = Implication(
            And(Variable('P'), Truth()),
            Or(Not(Falsity()), Variable('Q'))
        )
    
        print("Testing structure and pretty printing:")
        print(formula)
        
    except Exception as e:
        print(f"An error occurred: {e}")