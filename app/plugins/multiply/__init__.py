import logging

from app.commands import Command


class MultiplyCommand(Command):
    def execute(self, *args):
        try:
            if len(args) != 2:
                print("Invalid number of arguments for multiply command")
                logging.warning("Invalid number of arguments for multiply command")
                return

            a, b = map(float, args)  # Convert arguments to float
            result = a * b
            print(f"Result: {result}")
            logging.info(f"Multiplication result: {a} * {b} = {result}")
        except ValueError as e:
            print(f"Error: {str(e)}")
            logging.error(f"Error in multiply command: {str(e)}")
