import time
import signal
from functools import wraps
from ..Equivalence_Applier.applier import apply_equivalences


def timeout(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutError(f"Function call timed out after {seconds} seconds")
            
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return wrapper
    return decorator


@timeout(10)


def timed_apply_equivalences(formula, complexity_threshold, max_depth):
    return apply_equivalences(formula, complexity_threshold, max_depth)


def run_performance_tests():
    test_cases = [
        ("A & B", "!,&,|"),
        ("A | B", "!,&,|"),
        ("A -> B", "!,&,|,->"),
        ("F(A)", "!,&,|,F"),
        ("G(A & B)", "!,&,|,G"),
    ]
    
    complexity_threshold = 2.0
    max_depth = 2

    results = []
    for formula, operators in test_cases:
        try:
            start_time = time.time()
            equivalents = timed_apply_equivalences(formula, complexity_threshold, max_depth)
            end_time = time.time()
            execution_time = end_time - start_time
            results.append({
                'formula': formula,
                'operators': operators,
                'execution_time': execution_time,
                'num_equivalents': len(equivalents),
                'status': 'Completed'
            })
        except TimeoutError:
            results.append({
                'formula': formula,
                'operators': operators,
                'execution_time': 10,
                'num_equivalents': 'N/A',
                'status': 'Timeout'
            })

    print("\nPerformance Test Results:")
    print("=" * 50)
    for result in results:
        print(f"Formula: {result['formula']}")
        print(f"Operators: {result['operators']}")
        print(f"Execution time: {result['execution_time']:.4f} seconds")
        print(f"Number of equivalents: {result['num_equivalents']}")
        print(f"Status: {result['status']}")
        print("-" * 50)