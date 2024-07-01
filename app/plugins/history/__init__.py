import logging
from app.commands import Command
import os

class HistoryCommand(Command):
    def execute(self, *args):
        log_file_path = os.path.join('logs', 'app.log')
        try:
            with open(log_file_path, 'r') as log_file:
                print("Calculation history:")
                for line in log_file:
                    if "Addition result:" in line:
                        print(line.strip())
        except FileNotFoundError:
            print("Log file not found.")
