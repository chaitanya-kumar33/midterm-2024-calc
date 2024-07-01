import logging
from app.commands import Command
import os

import os

import importlib
import importlib
from app.commands import Command

class LoadCommand(Command):
    def execute(self, *args):
        if len(args) != 1:
            print("Invalid number of arguments. Usage: load <plugin_name>")
            return
        
        plugin_name = args[0]
        try:
            # Import the plugin dynamically
            plugin_module = importlib.import_module(f"app.plugins.{plugin_name}")
            # Get the commands from the plugin module
            plugin_commands = getattr(plugin_module, 'commands', None)
            if plugin_commands is None or not isinstance(plugin_commands, dict):
                print(f"Plugin '{plugin_name}' loaded successfully.")
                return

            # Register the commands from the plugin
            for command_name, command_class in plugin_commands.items():
                handler.register_command(command_name, command_class())
            print(f"Plugin '{plugin_name}' loaded successfully.")
        except ModuleNotFoundError:
            print(f"Plugin '{plugin_name}' not found.")
