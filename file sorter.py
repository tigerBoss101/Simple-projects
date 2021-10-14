"""
File sorter V 1.0.1
"""

import os
import shutil
from itertools import groupby


def main(target_path: str) -> None:
    filter_types = ["jpg", "png", "mp4"]
    files = [f for f in os.listdir(target_path) if "." in f and f.split(".")[1] in filter_types]
    file_map = {key:list(group) for key, group in groupby(files, key=lambda file: file.split(".")[1])}

    for ext in file_map:
        ext_dir = f"{target_path}/{ext}"
        if not os.path.exists(ext_dir):
            os.makedirs(ext_dir)

        current_files = file_map[ext]
        for file in current_files:
            start = f"{target_path}/{file}"
            end = f"{target_path}/{ext}/{file}"
            shutil.move(start, end)


if __name__ == "__main__":
    path = "D:" # selected folder path
    main(path)