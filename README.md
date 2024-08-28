# Translator LTL: Logical Equivalence Generator and Filter

This project provides a tool for generating and filtering logically equivalent formulae in Linear Temporal Logic (LTL). It includes both a web interface and a command-line application. While designed primarily for use in a GR(1) context in Spectra, it has broader applications as well.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
   - [Core Functionality](#core-functionality)
   - [Web Interface](#web-interface)
   - [Command Line Interface](#command-line-interface)
   - [Parameters](#parameters)
   - [Flags Explained](#flags-explained)
   - [Supported Operators](#supported-operators)
   - [Additional Functionalities](#additional-functionalities)
3. [Testing](#testing)
   - [Test Components](#test-components)
   - [Running the Tests](#running-the-tests)
   - [Interactive Testing](#interactive-testing)
4. [Project Structure](#project-structure)
   - [Directory Descriptions](#test-components)
   - [Root Directory Files](#root-directory-files)

## Installation

You can install this project in two ways:

1. Clone the repository:
```
git clone https://github.com/AryD05/Translator.git
cd Translator
```

2. Install using pip:
```
pip install -i https://test.pypi.org/simple/ translator-AryD05
```

The only dependency for this project is Flask, which is required to run the web application. To install Flask, run:
```
pip install flask
```

After installation, no additional setup is required. However, ensure you have Python 3.7 or later installed on your system.

If you've cloned the repository and want to run the project from the source, you might need to install the project in editable mode:
```
pip install -e
```

This will install the project and its dependencies based on the `pyproject.toml` file.

## Usage

### Core Functionality

At its core, this tool generates and filters logical equivalences for Linear Temporal Logic (LTL) formulae. It can:

1. Generate equivalent LTL formulae based on a given input formula.
2. Filter these equivalences based on specified logical operators.
3. Apply various complexity and depth constraints to the generation process.

The tool does not verify the correctness of input formulae. Ensure your input is valid to avoid nonsensical outputs.

Note: Both web application and command line application have been developed and tested on macOS. While they may work on other operating systems, full functionality is not guaranteed. Some adjustments might be necessary for Windows or Linux environments

### Web Interface

To launch the web interface, use the following command:

```
translator_launch
```

This starts a Flask server hosting the web application. Open your web browser and navigate to `http://127.0.0.1:8080/` to access the interface.

### Command Line Interface

To use the command-line interface, use the `translator_transform` command with the following syntax:

```
translator_transform "formula" operators complexity depth show_unfiltered timeout
```

#### Parameters

1. `formula`: The LTL formula enclosed in quotes (e.g., "A <-> B")
2. `operators`: Comma-separated list of allowed operators (e.g., \!,&,\|,->,<->,X,F,G,U,R,1,0)
   Note: Use \! for the NOT operator and \| for the OR operator to avoid shell interpretation.
   1 truth and 0 is falsity
3. `complexity`: Float value determining the relative complexity of generated equivalences (e.g., 2.5). Controls the intricacy of generated equivalences.
4. `depth`: Integer value setting the maximum depth of the equivalence tree (e.g., 3)
5. `show_unfiltered`: 'y' to show unfiltered results, 'n' to hide them
6. `timeout`: Float value setting the maximum execution time in seconds (e.g., 5.0)

#### Flags Explained

- **Complexity**: Controls the intricacy of generated equivalences relative to the complexity of the input formula. Higher values allow more complex transformations but increase processing time.
- **Depth**: Limits the recursive depth of equivalence generation. Higher values explore more possibilities but may significantly increase computation time.
- **Show Unfiltered**: When set to 'y', displays all generated equivalences before applying operator-based filtering.
- **Timeout**: Sets a time limit for the equivalence generation process to prevent excessively long computations.

### Supported Operators

- Propositional: ! (NOT), & (AND), | (OR), -> (IMPLIES), <-> (EQUIVALENT), 1 (TRUE), 0 (FALSE)
- Temporal: X (NEXT), F (EVENTUALLY), G (GLOBALLY), U (UNTIL), R (RELEASE)

### Additional Functionalities

1. Formula Parsing and Validation: Includes a robust parser for LTL formulae, ensuring correct interpretation of input.
2. Compile-time operator reachability check: Warns users if specified operators might not be sufficient to reach all possible operator inputs, and outputs the operators which might not be reachable.
3. Timeout Mechanism: Prevents excessively long computations by setting a time limit on the generation process.
4. Unfiltered Results Display: Option to view all generated equivalences before applying operator-based filtering.
5. Unit Testing: Includes scripts to test individual components of the tool.
6. Performance Testing: Includes a script to assess the efficiency of the equivalence generation process.

## Testing

The project includes a comprehensive test suite to ensure the correctness and performance of various components. The tests are located in the `Testing` directory and cover different aspects of the application.

### Test Components

1. **Structure Tests** (`test_structure.py`): Verify the correctness of the basic structures used in the project.

2. **Parser Tests** (`test_parser.py`): Ensure that the parser correctly interprets Linear Temporal Logic (LTL) formulae.

3. **Equivalence Applier Tests** (`test_equivalence_applier.py`): Check the functionality of applying equivalences to LTL formulae.

4. **Filter Tests** (`test_filter.py`): Validate the filtering mechanism for generated equivalences.

5. **Equivalences Tests** (`test_equivalences.py`): Test the correctness of predefined equivalences.

6. **Performance Tests** (`performance_test.py`): Evaluate the efficiency of the equivalence generation process.

### Running the Tests

To run all tests, navigate to the project root directory and execute the `test.py` file:

```
python test.py
```

This script will run through all test components, including:

- Parser testing
- Equivalence Applier testing
- Filter testing
- Equivalences testing
- Performance testing

The performance tests use a timeout mechanism to prevent excessively long computations. They evaluate the application's performance with various LTL formulae and operator sets.

### Interactive Testing

You can also test the application interactively using the command-line interface. To start the interactive shell, run:

```python
from translator.command_line import EquivalenceApplier
EquivalenceApplier().cmdloop()
```

This will start an interactive session where you can input commands to generate and filter equivalences. Use the `transform` command with the following syntax:

```
transform "formula" operators complexity depth show_unfiltered timeout
```

For example:
```
transform "A <-> B" \!,&,|,1,0 2.5 3 y 5.0
```

This command will generate equivalences for the formula "A <-> B", using the operators !, &, |, 1, and 0, with a complexity of 2.5, a maximum depth of 3, showing unfiltered results, and a timeout of 5 seconds.

## Project Structure

The project is organized into several directories and files, each serving a specific purpose. Here's an overview of the project structure:

```
translator_AryD05/
│
├── Equivalence_Applier/
│   ├── __init__.py
│   ├── applier.py
│   ├── equivalences.py
│   └── filter.py
│
├── Formula/
│   ├── __init__.py
│   ├── parser.py
│   ├── reverse_parser.py
│   └── structure.py
│
├── Testing/
│   ├── performance_test.py
│   ├── test_equivalence_applier.py
│   ├── test_equivalences.py
│   ├── test_filter.py
│   ├── test_parser.py
│   └── test_structure.py
│
├── Web_Interface/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   └── web_interface.py
│
├── __init__.py
├── command_line.py
├── test.py
├── .gitignore
├── LICENSE.txt
├── pyproject.toml
└── README.md
```

### Directory Descriptions

- **Equivalence_Applier/**: Contains the core logic for applying and filtering equivalences.
  - `applier.py`: Implements the equivalence application algorithm.
  - `equivalences.py`: Defines the set of logical equivalences used in the project.
  - `filter.py`: Handles filtering of generated equivalences.

- **Formula/**: Manages the parsing and structure of logical formulas.
  - `parser.py`: Implements the parser for logical formulas.
  - `reverse_parser.py`: Handles reverse parsing of logical structures.
  - `structure.py`: Defines the structure of logical formulas.

- **Testing/**: Contains all test files for various components of the project.
  - Includes tests for equivalence applier, parser, filter, and performance.

- **Web_Interface/**: Houses the web application components.
  - `static/`: Contains a CSS static file for the web interface.
  - `templates/`: Stores a HTML template for the web interface.
  - `web_interface.py`: Implements the web application logic.

### Root Directory Files

- `__init__.py`: Marks the directory as a Python package.
- `command_line.py`: Implements the command-line interface for the application.
- `test.py`: Main test runner script.
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `LICENSE.txt`: Contains the license information for the project.
- `pyproject.toml`: Defines the project metadata and dependencies.
- `README.md`: Provides an overview and documentation for the project.

This structure organizes the project into logical components, separating core functionality, testing, and user interfaces (both web and command-line). It facilitates easy navigation and main  tenance of the codebase.