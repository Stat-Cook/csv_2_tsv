import os
from collections import UserString

from .utils import reader_dict, writer_dict


class FilePath(UserString):

    def __init__(self, file_path: str, write_ext: str = ".tsv"):
        self.file, self.file_ext = os.path.splitext(file_path)
        super().__init__(file_path)

        self._write_ext = write_ext

    def to_file(self, sheet: str = None):

        if (sheet == "Sheet1") or sheet is None:
            return f"{self.file}{self._write_ext}"
        else:
            return f"{self.file} {sheet}{self._write_ext}"

    @property
    def reader(self):
        return reader_dict[self.file_ext]

    @property
    def writer(self):
        return writer_dict[self._write_ext]


def convert(file: str, write_ext: str = ".tsv", new_data_dir=None):
    new_data_dir = new_data_dir or ""

    fp = FilePath(file, write_ext)
    data = fp.reader(file)

    if isinstance(data, dict):
        for sheet, data in data.items():
            write_file = fp.to_file(sheet)
            write_file = os.path.join(new_data_dir, write_file)
            fp.writer(data, write_file)

    else:
        write_file = fp.to_file()
        write_file = os.path.join(new_data_dir, write_file)
        fp.writer(data, write_file)



    return fp.to_file
