import logging

from app.commands import Command


class DivideCommand(Command):
    def execute(self, *args):
        try:
            if len(args) != 2:
                print("Invalid number of arguments for divide command")
                logging.warning("Invalid number of arguments for divide command")
                return

            a, b = map(float, args)  # Convert arguments to float
            if b == 0:
                print("Error: Division by zero")
                logging.error("Division by zero")
                return
            result = a / b
            print(f"Result: {result}")
            logging.info(f"Division result: {a} / {b} = {result}")
        except ValueError as e:
            print(f"Error: {str(e)}")
            logging.error(f"Error in divide command: {str(e)}")
