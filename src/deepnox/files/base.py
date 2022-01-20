import os
from typing import List


# https://www.sethserver.com/python/recursively-list-files.html


def get_all_files_recursively_from_directory(dirname: str) -> List[str]:
    """
    Get all files recursively from a directory.

    :param dirname: The directory name.
    :type dirname: str
    :return: The list of founded files.
    :rtype: List[str]
    """
    files = []
    for (dirpath, dirnames, filenames) in os.walk(dirname):
        files.extend(
            map(
                lambda n: os.path.join(*n),
                zip([dirpath] * len(filenames), filenames),
            )
        )
    return files
