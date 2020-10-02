import sys
import os


def extend_paths(cwd="."):
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
