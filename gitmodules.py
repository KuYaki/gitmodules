__author__ = 'kuyaki'
__copyright__ = '2020 KuYaki'
__credits__ = ['kuyaki']
__maintainer__ = 'kuyaki'
__date__ = '2020/10/02'
__version__ = '0.1'

import sys
import os


def extend_paths(cwd="."):
    """
    This function tries to find .gitmodules file in your project,
    parse it and append all the git submodules directories to the 'sys.path'.
    After what it recursively repeat this action for all the git submodules.
    :param cwd: current work directory where the '.gitmodules' file should be placed
    :return: None
    """
    git_modules_file_path = os.path.join(cwd, ".gitmodules")
    if os.path.exists(git_modules_file_path):
        with open(git_modules_file_path) as f:
            for line in f.readlines():
                if "path = " in line:
                    path = line.split("path = ")[-1][:-1]
                    git_module_path = os.path.join(cwd, path)
                    if os.path.exists(git_module_path):
                        sys.path.append(git_module_path)
                        extend_paths(git_module_path)


extend_paths()
