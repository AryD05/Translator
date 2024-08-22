'''
This module provides a command-line tool for generating and filtering equivalences for a given logical formula.
'''



import cmd
import threading
from itertools import chain, combinations
from .Equivalence_Applier.filter import filter_equivalences
from .Equivalence_Applier.applier import apply_equivalences
import sys


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def check_dependencies(operators):
    dependencies = {
        '!': [{'!'}],
        '&': [{'&'}, {'!', '|'}, {'!', '->'}],
        '|': [{'|'}, {'!', '&'}, {'!', '->'}],
        '->': [{'->'}, {'!', '|'}, {'!', '&'}],
        '<->': [{'<->'}, {'!', '&'}, {'!', '|'}, {'!', '->'}, {'&', '->'}],
        'X': [{'X'}],
        'F': [{'F'}, {'U'}, {'G', '!'}],
        'G': [{'G'}, {'F', '!'}, {'U', '!'}],
        'U': [{'U'}],
        'R': [{'R'}, {'U', '!'}, {'F', 'G'}, {'U', 'G'}, {'F', '!'}],
        '1': [{'1'}, {'0', '!'}, {'->'}, {'!', '&'}, {'!', '|'}],
        '0': [{'0'}, {'1', '!'}, {'!', '->'}, {'!', '&'}, {'!', '|'}]
    }
    
    reachable = set(operators)
    changed = True
    while changed:
        changed = False
        for op, dep_sets in dependencies.items():
            if op not in reachable:
                for dep_set in dep_sets:
                    if dep_set.issubset(reachable):
                        reachable.add(op)
                        changed = True
                        break
    
    unreachable = set(dependencies.keys()) - reachable
    return unreachable


def parse_command(command: str) -> tuple:
    '''
    Parse a user command into its components.

    @param command: The user input command string
    @return: A tuple containing the parsed components (formula, operators, complexity, depth, show_unfiltered, timeout)
    '''

    parts = command.split('"')
    if len(parts) != 3 or len(parts[1].strip()) == 0:
        raise ValueError("Invalid formula format. Formula must be enclosed in double quotes e.g. transform \"A <-> B\" ->,&,1,0 2.5 3 y 5.0")

    formula = parts[1].strip()
    remaining_parts = parts[2].strip().split()

    if len(remaining_parts) != 5:
        raise ValueError("Invalid command format. Check that all arguments are included correctly e.g. transform \"A <-> B\" ->,&,1,0 2.5 3 y 5.0")

    operators = set()
    for op_str in remaining_parts[0].split(','):
        if op_str == '!':
            operators.add('!')
        else:
            operators.add(op_str)

    if not all(op in {'!', '&', '|', '->', '<->', 'X', 'F', 'G', 'U', 'R', '1', '0'} for op in operators):
        raise ValueError("Invalid operators. Use any combination of !, &, |, ->, <->, X, F, G, U, R, 1, 0")

    try:
        complexity = float(remaining_parts[1])
    except ValueError:
        raise ValueError("Complexity must be a float.")

    try:
        depth = int(remaining_parts[2])
    except ValueError:
        raise ValueError("Depth must be an integer.")

    show_unfiltered = remaining_parts[3].lower()
    if show_unfiltered not in {'y', 'n'}:
        raise ValueError("Show unfiltered must be 'y' or 'n'.")

    try:
        timeout = float(remaining_parts[4])
    except ValueError:
        raise ValueError("Timeout must be a float.")

    return formula, operators, complexity, depth, show_unfiltered == 'y', timeout


class EquivalenceApplier(cmd.Cmd):
    intro = "Welcome to the equivalence applier. Type help or ? to list commands.\n"
    prompt = "(equivalence) "
    

    def do_transform(self, arg):
        '''
        Generate and filter equivalences.
        Supported operators: !, &, |, ->, <->, X, F, G, U, R, 1 (truth), and 0 (falsity)
        Please input ! and | as \! and \|

        Input format: transform "formula" operators complexity depth show_unfiltered timeout
        Example: transform "A <-> B" \!,&,->,1 2.5 3 n 5.0
        '''

        if not arg:
            print("Please provide arguments. Use 'help transform' for usage information.")
            return
        
        try:
            formula, operators, complexity, depth, show_unfiltered, timeout = parse_command(arg)
            print(f"Formula: {formula}, Operators: {operators}, Complexity: {complexity}, Depth: {depth}, Show Unfiltered: {show_unfiltered}, Timeout: {timeout}")
            
            unreachable = check_dependencies(operators)
            if unreachable:
                print(f"Warning: The following operators might not always be reachable: {', '.join(unreachable)}. Consider augmenting your list of available operators.")
        except ValueError as e:
            print(f"Error in command: {str(e)}")
            return

        result = []
        exception = []

        def run_apply_equivalences():
            try:
                result.append(apply_equivalences(formula, complexity, depth))
            except Exception as e:
                exception.append(e)

        thread = threading.Thread(target=run_apply_equivalences)
        thread.start()
        thread.join(timeout)

        if thread.is_alive():
            print(f"Timeout: Equivalence generation took longer than {timeout} seconds. Consider reducing complexity and/or depth.")
            return

        if exception:
            print(f"An error occurred: {exception[0]}")
            return

        equivalents = result[0]

        if show_unfiltered:
            print(f"\nBefore filtering: {len(equivalents)}")
            for eq in equivalents:
                print(eq._str())

        # Filter equivalences
        filtered_equivalents = filter_equivalences(equivalents, operators)

        if len(filtered_equivalents) == 0:
            print(f"No equivalent statements generated after filtering. Consider increasing complexity and/or depth, or increasing the list of available operators.")
        else:
            print(f"After filtering: {len(filtered_equivalents)}")
            for eq in filtered_equivalents:
                print(eq._str())


    def do_exit(self, arg):
        '''
        Exit the application.

        @param arg: Unused argument
        @return: True to signal the application to exit
        '''
        
        print("Exiting...")
        return True
    

def run_transform_command():
    '''
    Runs the transform command from the command line.

    This function initialises the EquivalenceApplier and processes
    the command line arguments to perform the transformation.
    It's designed to be called as an entry point for the
    translator_transform command.
    '''
    
    if len(sys.argv) != 7:
        print("Invalid command format. Check that all arguments are included correctly e.g. transform \"A <-> B\" \\!,&,|,1,0 2.5 3 y 5.0")
        return

    try:
        formula = sys.argv[1]
        operators = sys.argv[2]
        complexity = sys.argv[3]
        depth = sys.argv[4]
        show_unfiltered = sys.argv[5]
        timeout = sys.argv[6]

        command = f'transform "{formula}" {operators} {complexity} {depth} {show_unfiltered} {timeout}'
        cmd = EquivalenceApplier()
        cmd.onecmd(command)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_transform_command()