import logging
from app.commands import Command
import os

import os

class ClearCommand(Command):
    def execute(self, *args):
        log_file_path = os.path.join('logs', 'app.log')
        try:
            # Open the log file in write mode to clear its contents
            with open(log_file_path, 'w'):
                pass  # Just open and close the file to clear its contents
            print("Calculation history cleared.")
        except FileNotFoundError:
            print("Log file not found.")

