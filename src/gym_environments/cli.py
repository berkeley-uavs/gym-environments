"""Module that contains the command line application."""

import argparse
from numpy.ctypeslib import load_library
from gym_environments.examples.designs import export_design_json, load_design_json
from typing import List, Optional
from gym_environments.examples.library import *


def get_parser() -> argparse.ArgumentParser:
    """
    Return the CLI argument parser.

    Returns:
        An argparse parser.
    """
    return argparse.ArgumentParser(prog="gym-environments")


def main_script() -> int:
    parser = get_parser()
    opts = parser.parse_args(args=args)
    print(f"script called with arguments: {opts}")
    return 0
