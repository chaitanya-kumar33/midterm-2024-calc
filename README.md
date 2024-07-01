# Advanced Python Calculator for Software Engineering Graduate Course

## Project Overview

This midterm requires the development of an advanced Python-based calculator application. Designed to underscore the importance of professional software development practices, the application integrates clean, maintainable code, the application of design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Design Patterns](#design-patterns)
- [Logging](#logging)
- [Contributing](#contributing)

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

  
## Installation

1. Clone the repository:

```
git clone https://github.com/
```

2. Navigate to the project directory:

```
cd advanced-python-calculator
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

To start the calculator, run the following command:

```
python main.py
```

This will launch the REPL interface, where you can perform arithmetic operations, manage calculation history, and access additional functionalities through plugins.

### Commands

- `add <operand1> <operand2>`: Performs addition of two numbers.
- `subtract <operand1> <operand2>`: Performs subtraction of two numbers.
- `multiply <operand1> <operand2>`: Performs multiplication of two numbers.
- `divide <operand1> <operand2>`: Performs division of two numbers.
- `history`: Displays the calculation history.
- `clear`: Clears the calculation history.
- `load <plugin_name>`: Loads a plugin and makes its commands available.
- `plugins`: Lists all available plugins and their commands.
- `exit`: Exits the calculator application.

### Plugins

The calculator supports dynamic loading of plugins. To load a plugin, use the `load <plugin_name>` command. Once a plugin is loaded, its commands become available within the REPL.

## Features

- **Command-Line Interface (REPL)**: An interactive environment for performing arithmetic operations and managing calculation history.
- **Plugin System**: A system to extend functionalities through dynamically loaded plugins.
- **Calculation History Management with Pandas**: Leverages Pandas for robust management and manipulation of calculation history.
- **Comprehensive Logging**: Implements detailed logging for operations, errors, and informational messages.
- **Design Patterns**: Utilizes Facade, Command, Factory Method, Singleton, and Strategy Patterns for a scalable and flexible architecture.
  
The design patterns used in this project promote modularity, extensibility, and maintainability. For more details on their implementation and impact, please refer to the respective sections in the source code.

## Logging

The calculator application uses a comprehensive logging system to record detailed application operations, data manipulations, errors, and informational messages. The logging system supports different log levels (INFO, WARNING, ERROR) and can be configured to output logs to various destinations (console, file) through environment variables.

The following environment variables can be used to configure logging:

- `LOGGING_LEVEL`: Sets the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
- `LOGGING_FILE`: Specifies the file path for logging output.

## Testing

Run the following command to execute tests and ensure the application behaves as expected:

```bash
pytest
```

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.


## Acknowledgments

- [Python](https://www.python.org/) - The core programming language used.
- [Pandas](https://pandas.pydata.org/) - Utilized for data handling and calculation history management.
- [Pytest](https://docs.pytest.org/en/stable/) - The testing framework used.

