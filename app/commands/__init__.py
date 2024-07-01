from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class AddCommand(Command):
    def execute(self, *args):
        if len(args) == 2:
            try:
                num1 = float(args[0])
                num2 = float(args[1])
                result = num1 + num2
                print(f"The result of adding {num1} and {num2} is: {result}")
            except ValueError:
                print("Invalid numbers provided.")
        else:
            print("Invalid number of arguments provided.")

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_input: str):
        command_parts = command_input.split()
        command_name = command_parts[0]
        args = command_parts[1:]
        try:
            self.commands[command_name].execute(*args)
        except (KeyError, TypeError):
            print(f"No such command: {command_input}")

# Example usage
if __name__ == "__main__":
    handler = CommandHandler()
    handler.register_command("add", AddCommand)
    
    while True:
        command_input = input(">>> ")
        if command_input == "exit":
            break
        handler.execute_command(command_input)
