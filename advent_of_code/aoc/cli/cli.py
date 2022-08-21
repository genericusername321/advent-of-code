import argparse

from advent_of_code.aoc.prepare_solution.prepare_solution import prepare_solution_dir
from advent_of_code.aoc.runner.runner import run_solution


def prepare_solution_dir_wrapper(args: argparse.Namespace) -> None:

    prepare_solution_dir(args.year, args.day)


def run_wrapper(args: argparse.Namespace) -> None:

    run_solution(args.year, args.day)


def generate_parser():

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()
    get_parser = subparsers.add_parser("prepare")
    get_parser.add_argument("year", type=int)
    get_parser.add_argument("day", type=int)
    get_parser.set_defaults(_func=prepare_solution_dir_wrapper)

    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("year", type=int)
    run_parser.add_argument("day", type=int)
    run_parser.set_defaults(_func=run_wrapper)

    return parser
