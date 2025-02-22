"""
Simple script to print the application version.

This script defines a version constant and prints the app version
when executed. It exits with a status code of 0.
"""

import sys

VERSION = "v0.0.1"


def print_version():
    """Prints the application version and exits."""
    print(f"App Version: {VERSION}")
    sys.exit(0)


if __name__ == "__main__":
    print_version()
