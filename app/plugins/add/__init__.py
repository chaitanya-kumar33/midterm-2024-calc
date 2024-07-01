import logging
import os
from app.commands import Command
import pandas as pd




class AddCommand(Command):
    def execute(self, *args):
        try:
            if len(args) != 2:
                print("Invalid number of arguments for add command")
                logging.warning("Invalid number of arguments for add command")
                return

            a, b = map(float, args)  # Convert arguments to float
            result = a + b
            print(f"Result: {result}")
            logging.info(f"Addition result: {a} + {b} = {result}")
        except ValueError as e:
            print(f"Error: {str(e)}")
            logging.error(f"Error in add command: {str(e)}")
