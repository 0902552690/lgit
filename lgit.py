#!/usr/bin/env python3
from argparse import ArgumentParser
from lgit_functions import *


def createParser():
    """
    Create a parser for the program
    """
    # Create a base parser with an usage message
    parser = ArgumentParser(usage="./lgit.py <command> [<args>]")
    # Create a subparser group that will be used to parse each command
    subparsers = parser.add_subparsers(dest="command")
    # Create a subparser for init command
    init_parser = subparsers.add_parser("init")
    # Create a subparser for add command
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("filenames", nargs="+")
    # Create a subparser for remove command
    remove_parser = subparsers.add_parser("remove")
    remove_parser.add_argument("filenames", nargs="+")
    # Create a subparser for commit command
    commit_parser = subparsers.add_parser("commit")
    commit_parser.add_argument("-m", dest="message", nargs=1, required=True)
    # Create a subparser for log command
    log_parser = subparsers.add_parser("log")
    # Create a subparser for config command
    config_parser = subparsers.add_parser("config")
    config_parser.add_argument("--author", nargs=1, required=True)
    # Create a subparser for ls-files command
    list_files_parser = subparsers.add_parser("ls-files")
    # Create a subparser for status command
    status_parser = subparsers.add_parser("status")
    # Return the base parser
    return parser


def main():
    # Create a parser
    parser = createParser()
    # Parse the argument
    args = parser.parse_args()
    # Dictionary contains all the functions that each command will execute
    functionDict = {"init": init_lgit,
                    "add": add_lgit,
                    "rm": remove_lgit,
                    "commit": commit_lgit,
                    "config": config_lgit,
                    "ls-files": list_files_lgit,
                    "log": show_log_lgit,
                    "status": show_status_lgit
                    }
    print(args)
    # Pass the argument to the respective function to execute
    functionDict[args.command](args)


if __name__ == "__main__":
    main()
