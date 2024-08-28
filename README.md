# Translator LTL: Logical Equivalence Generator and Filter

This project provides a tool for generating and filtering logical equivalences for Linear Temporal Logic (LTL) formulas. It includes both a web interface and a command-line application. While designed primarily for use in a GR(1) context in Spectra, it has broader applications as well.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
   - [Web Interface](#web-interface)
   - [Command Line Interface](#command-line-interface)
   - [Parameters] (#parameters)
   - [Flags Explained] (#flags-explained)
   - [Supported Operators] (#supported-operators)
3. [Additional Functionality](#additional-functionalities)
4. [Notes](#important-notes)
5. [Testing](#testing)
6. [Project Structure](#project-structure)

## Installation

You can install this project in two ways:

1. Clone the repository:
git clone https://github.com/AryD05/Translator.git
cd Translator

2. Install using pip:
pip install -i https://test.pypi.org/simple/ translator-AryD05

The only dependency for this project is Flask, which is required to run the web application. To install Flask, run:
pip install flask

After installation, no additional setup is required. However, ensure you have Python 3.7 or later installed on your system.

If you've cloned the repository and want to run the project from the source, you might need to install the project in editable mode:
pip install -e

This will install the project and its dependencies based on the `pyproject.toml` file.

## Usage

### Core Functionality

At its core, this tool generates and filters logical equivalences for Linear Temporal Logic (LTL) formulae. It can:

1. Generate equivalent LTL formulas based on a given input formula.
2. Filter these equivalences based on specified logical operators.
3. Apply various complexity and depth constraints to the generation process.

The tool does not verify the correctness of input formulas. Ensure your input is valid to avoid nonsensical outputs.

### Web Interface

To launch the web interface, use the following command:

translator_launch

This starts a Flask server hosting the web application. Open your web browser and navigate to `http://127.0.0.1:8080/` to access the interface.

### Command Line Interface

To use the command-line interface, use the `translator_transform` command with the following syntax:

translator_transform "formula" operators complexity depth show_unfiltered timeout

#### Parameters:

1. `formula`: The LTL formula enclosed in quotes (e.g., "A <-> B")
2. `operators`: Comma-separated list of allowed operators (e.g., \!,&,\|,->,<->,X,F,G,U,R,1,0)
   Note: Use \! for the NOT operator and \| for the OR operator to avoid shell interpretation.
   1 truth and 0 is falsity
3. `complexity`: Float value determining the relative complexity of generated equivalences (e.g., 2.5). Controls the intricacy of generated equivalences.
4. `depth`: Integer value setting the maximum depth of the equivalence tree (e.g., 3)
5. `show_unfiltered`: 'y' to show unfiltered results, 'n' to hide them
6. `timeout`: Float value setting the maximum execution time in seconds (e.g., 5.0)

#### Flags Explained:

- **Complexity**: Controls the intricacy of generated equivalences. Higher values allow more complex transformations but increase processing time.
- **Depth**: Limits the recursive depth of equivalence generation. Higher values explore more possibilities but may significantly increase computation time.
- **Show Unfiltered**: When set to 'y', displays all generated equivalences before applying operator-based filtering.
- **Timeout**: Sets a time limit for the equivalence generation process to prevent excessively long computations.

### Supported Operators:

- Propositional: ! (NOT), & (AND), | (OR), -> (IMPLIES), <-> (EQUIVALENT), 1 (TRUE), 0 (FALSE)
- Temporal: X (NEXT), F (EVENTUALLY), G (GLOBALLY), U (UNTIL), R (RELEASE)

## Notes

Note: Both web application and command line application have been developed and tested on macOS. While they may work on other operating systems, full functionality is not guaranteed. Some adjustments might be necessary for Windows or Linux environments