import argparse

from utils.download_inputs import get_problem_input


def get_problem_input_wrapper(args: argparse.Namespace) -> None:

    get_problem_input(args.year, args.day)


def generate_parser():

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()
    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("year", type=int)
    get_parser.add_argument("day", type=int)
    get_parser.set_defaults(_func=get_problem_input_wrapper)

    return parser
