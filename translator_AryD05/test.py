from Testing.test_structure import test_structure
from Testing.test_parser import test_parser
from Testing.test_equivalence_applier import test_equivalence_applier
from Testing.test_filter import test_filter
from Testing.test_equivalences import test_equivalences
from Testing.performance_test import run_performance_tests
from translator_AryD05.command_line import EquivalenceApplier


def main():
    
    input = "A <-> B"

    print("Testing Parser:")  
    test_parser(input)
    print("\n" + "="*50 + "\n")

    print("Testing Equivalence Applier:")    
    test_equivalence_applier(input)
    print("\n" + "="*50 + "\n")

    print("Testing Filter:")
    test_filter(input)
    print("\n" + "="*50 + "\n")

    print("Testing Equivalences:")
    passed, failed = test_equivalences()
    print(f"\nEquivalence Tests - Passed: {passed}, Failed: {failed}")
    
    print("Performance test:")
    run_performance_tests()


if __name__ == '__main__':
    #main()
    EquivalenceApplier().cmdloop()