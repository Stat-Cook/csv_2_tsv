import os

from csv_2_tsv import convert

def spider(root: str = ""):
    root = root or None
    walk = os.walk(root)

    for root, dirs, files in walk:
        csv_files = [i for i in files if i.endswith(".csv")]

        for csv_file in csv_files:
            file_path = os.path.join(root, csv_file)
            print(convert(file_path))

