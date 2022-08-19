import argparse
from utils.cli import generate_parser

if __name__ == "__main__":

    parser: argparse.ArgumentParser = generate_parser()
    args = parser.parse_args()
    args._func(args)
