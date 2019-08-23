"""
Author: Saad Zaher <eng.szaher@gmail.com>

"""

import argparse
import logging
import sys

LOG = logging.getLogger(__name__)


def setup_args(args=[]):
    parser = argparse.ArgumentParser(prog="{{ cookiecutter.program_name }}", description="{{ cookiecutter.service }}")
    parser.add_argument("-d", "--debug", help="Enable debugging", action="store_true")
    parser.add_argument("--log-file", help="Log file")
    parser.add_argument("--log-level",
                        choices=["debug", "critical", "info", "warning", "error"],
                        default=logging.INFO,
                        help="Log level")
    if not args:
        parser.print_usage()
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()


def setup_logging(log_file, log_level):
    """
    Add logging configuration here
    :param log_file: file to append loggings
    :param log_level: Log level
    :return:
    """
    if log_level == "debug":
        log_level = logging.DEBUG
    elif log_level == "critical":
        log_level = logging.CRITICAL
    elif log_level == "info":
        log_level = logging.INFO
    elif log_level == "warning":
        log_level = logging.WARNING
    elif log_level == "error":
        log_level = logging.ERROR
    else:
        log_level = logging.INFO
    logging.basicConfig(filename=log_file, level=log_level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    args = setup_args(sys.argv[1:])
    setup_logging(args.log_file, args.log_level)
    print("Welcome to {{ cookiecutter.service }} ")
