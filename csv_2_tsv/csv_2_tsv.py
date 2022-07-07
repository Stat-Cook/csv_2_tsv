import pandas as pd
from collections import UserString
import re

csv_pattern = re.compile(r"\.csv$")

class FilePath(UserString):

    def __init__(self, file_path: str):
        assert file_path.endswith(".csv")
        super().__init__(file_path)

    @property
    def tsv(self):
        return csv_pattern.sub(".tsv", self.data)


def convert(file: str):

    fp = FilePath(file)

    data = pd.read_csv(file)
    data.to_csv(fp.tsv, sep="\t", index=False)

    return fp.tsv
