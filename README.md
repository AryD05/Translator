# Translator LTL: Logical Equivalence Generator and Filter

This project provides a tool for generating and filtering logical equivalences for Linear Temporal Logic (LTL) formulas. It includes both a web interface and a command-line application. While designed primarily for use in a GR(1) context in Spectra, it has broader applications as well.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
   - [Web Interface](#web-interface)
   - [Command Line Interface](#command-line-interface)
3. [Functionalities](#functionalities)
4. [Important Notes](#important-notes)
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

Note: Both web application and command line application have been developed and tested on macOS. While it may work on other operating systems, full functionality is not guaranteed. Some adjustments might be necessary for Windows or Linux environments

After installation, no additional setup is required. However, ensure you have Python 3.7 or later installed on your system.

If you've cloned the repository and want to run the project from the source, you might need to install the project in editable mode:
pip install -e

This will install the project and its dependencies based on the `pyproject.toml` file.