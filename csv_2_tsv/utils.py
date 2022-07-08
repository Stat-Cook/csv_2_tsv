"""
Utility dictionaries used in the csv_2_tsv package.
"""

import pandas as pd

reader_dict = {
    ".csv": pd.read_csv,
    ".tsv": lambda path: pd.read_csv(path, sep="\t"),
    ".xls": lambda path: pd.read_excel(path, sheet_name=None),
    ".xlsb": lambda path: pd.read_excel(path, sheet_name=None),
    ".xlsx": lambda path: pd.read_excel(path, sheet_name=None)
}

writer_dict = {
    ".csv": lambda data, path: data.to_csv(path),
    ".tsv": lambda data, path: data.to_csv(path, sep="\t"),
    ".xls": lambda data, path: data.to_excel(path),
    ".xlsb": lambda data, path: data.to_excel(path),
    ".xlsx": lambda data, path: data.to_excel(path)
}
