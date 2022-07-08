"""
Implementation of directory crawler to find files and convert
"""
import os
import pathlib
import logging as log

from .convert import convert


def convert_spider(crawler_root: str = ".",
                   read_ext=".csv", write_ext: str = ".tsv", new_root: str = None,
                   verbose=False):
    """
    Crawl directory structure for files with a given extension and convert.

    Args:
        root: str [optional]
            Path to start crawler from.  By default uses working directory.
        read_ext: str [optional]
            File extensions to search for.
        write_ext: str [optional]
            File extensions to write to.
        new_root: str [optional]
            Root of directory structure to write converted files to with directory structure.
                By default files are created by the original files.
        verbose: bool [optional]
            TODO: implement logging
    """

    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info(f"Converting from '{read_ext}' to '{write_ext}' from root '{crawler_root}'")
        if new_root:
            log.info(f"New data written at root '{new_root}'")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")


    crawler_root = crawler_root or None
    new_data_dir = new_root or False

    walk = os.walk(crawler_root)

    for root, _, files in walk:
        data_files = [i for i in files if i.endswith(read_ext)]

        if data_files and new_data_dir:
            new_root = os.path.join(new_data_dir, root)
            path = pathlib.Path(new_root)
            path.mkdir(exist_ok=True, parents=True)

        for data_file in data_files:
            log.info(f"Converting file {data_file}")
            file_path = os.path.join(root, data_file)
            convert(file_path, write_ext, new_data_dir)
