import argparse
from csv_2_tsv import spider


def csv_2_tsv():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", help='Root path to start crawler from',
                        default=".", nargs="?")

    args = parser.parse_args()

    root_path = args.root

    spider(root_path)
    return 0
