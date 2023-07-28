# Stori challenge - Mariano Delfino
This is my solution for the challenge provided by the Stori team.

In case you would like to know something from this test, just let me know.

## Table of contents
-[Installation](#installation)

-[Usage](#usage)

-[Features](#features)


### Installation

Run the following commands in the terminal:

    1. python3 -m venv virtual_env
        To create a virtual environment. Not necessary but recommended.
    2. source virtual_env/bin/activate
        To move into the virtual environment.
    3. pip install -r requirements.txt
        Installs the requirements for the tests.

### Usage

Run the command pytest to execute the tests. Their results will show up in the file report.html.

The tests will run on Chrome by default, but could be run on firefox or opera by using the --browser command.

### Features

Every test in the RTM have their own test. The association between test and feature is explained in the RTM file.
