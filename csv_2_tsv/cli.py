"""
Implementation of the csv_2_tsv CLI interface.
"""

import argparse
from csv_2_tsv import convert_spider


def csv_2_tsv():
    """
    CLI to the csv_2_tsv.spider function.

    Returns:
        int
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("root", help='Root path to start crawler from',
                        default=".", nargs="?")

    parser.add_argument("-r", "--read_ext", help='File extension to read from',
                        default=".csv", nargs="?")

    parser.add_argument("-w", "--write_ext", help='File extension to write to',
                        default=".tsv", nargs="?")

    parser.add_argument("-n", "--new_path", help='Path to write data structure to [optional]',
                        default="", nargs="?")

    parser.add_argument("-v", "--verbose",
                        action = "store_true",
                        help='Turn on verbose logging [optional]')

    args = parser.parse_args()

    convert_spider(args.root, args.read_ext, args.write_ext, args.new_path, args.verbose)
    return 0
