"""
Implementation of conversion (read -> write) of a single data file.
"""
import os

from .file_path import FilePath


def convert(file: str, write_ext: str = ".tsv", new_data_dir=None):
    """
    Convert a file (read -> write) to a new data type.

    Args:
        file: str
            File path to original data set
        write_ext: str [optional]
            File type to write to, by default *.tsv*
        new_data_dir: str [optional]
            Root of new data directory.
            By default, converted data is written to the same location as `file`

    Returns:
        FilePath
    """
    new_data_dir = new_data_dir or ""

    file_path = FilePath(file, write_ext)
    data = file_path.reader(file)

    if isinstance(data, dict):
        for sheet, data in data.items():
            write_path = file_path.write_path(sheet)
            write_path = os.path.join(new_data_dir, write_path)
            file_path.writer(data, write_path)

    else:
        write_path = file_path.write_path()
        write_path = os.path.join(new_data_dir, write_path)
        file_path.writer(data, write_path)

    return file_path
