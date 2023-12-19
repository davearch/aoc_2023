# Advent of Code
# Usage - give it a day as an integer, and it will run that script

import sys
import os
import importlib

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <day>")
        sys.exit(1)

    day = sys.argv[1]
    try:
        day = int(day)
    except ValueError:
        print("Usage: python main.py <day>")
        sys.exit(1)

    module_name = f"aoc_day{day}"
    module_path = os.path.join(os.path.dirname(__file__), module_name)

    if not os.path.exists(module_path):
        print(f"Module for Day {day} not found at path: {module_path}")
        sys.exit(1)

    day_module = importlib.import_module(module_name + "." + module_name)

    if hasattr(day_module, 'main'):
        day_module.main()
    else:
        print(f"The module {module_name} does not have a 'main' function.")
