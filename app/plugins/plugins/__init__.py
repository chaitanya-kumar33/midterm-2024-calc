import logging
from app.commands import Command
import os

import os

import importlib
import importlib
from app.commands import Command
import os
import pkgutil

class ListPluginsCommand(Command):
    def execute(self, *args):
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        
        if not os.path.exists(plugins_path):
            print("No plugins found.")
            return
        
        print("Available plugins and commands:")
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                plugin_commands = getattr(plugin_module, 'commands', {})
                print(f"Plugin: {plugin_name}")
                for command_name, command_class in plugin_commands.items():
                    print(f"- Command: {command_name}")
