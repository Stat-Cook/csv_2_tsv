"""
Interface to extension dependent tools for manipulating files.
"""

import os
from collections import UserString

from .utils import reader_dict, writer_dict


class FilePath(UserString):
    """
    Representation of a file conversion.
    """

    def __init__(self, file_path: str, write_ext: str = ".tsv"):
        """
        Construct tools for manipulating file, dependent on file extension and write_ext.

        Args:
            file_path: str
                Path to file for reading
            write_ext: str [optional]
                Writing file extension.
        """

        self.file, self.file_ext = os.path.splitext(file_path)
        self.file_ext = self.file_ext.lower()
        super().__init__(file_path)

        self._write_ext = write_ext

    def write_path(self, sheet: str = None):
        """
        Generate file path for writing to.

        Args:
            sheet: str [optional]
                Spreadsheet optional argument.
                Sheet name to include in file names.  Ignores 'Sheet1'.

        Returns:
            str
        """

        if (sheet == "Sheet1") or sheet is None:
            return f"{self.file}{self._write_ext}"

        return f"{self.file} {sheet}{self._write_ext}"

    @property
    def reader(self):
        """
        Look up data read function dependent on file extension.
        Returns:
            function
        """
        return reader_dict[self.file_ext]

    @property
    def writer(self):
        """
        Look up data write function dependent on `write_ext`.
        Returns:
            function
        """
        return writer_dict[self._write_ext]
