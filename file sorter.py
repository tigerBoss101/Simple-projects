#file sorter V 1.0.0

from collections import defaultdict
import os
import shutil
filter_option = False
filter_types = ["jpg", "png", "mp4"]
test_path = "D:" # selected folder path
files = [f for f in os.listdir(test_path) if "." in f and f.split(".")[1] in filter_types]
file_map = defaultdict(list)
for f in files:
    file_map[f.split(".")[1]].append(f)
file_map = dict(file_map)
for ext in file_map:
    if not os.path.exists(test_path + "/" + ext):
        os.makedirs(test_path + "/" + ext)
for ext in file_map:
    current_files = file_map[ext]
    for f in current_files:
        start = test_path + "/" + f
        end = test_path + "/" + ext + "/" + f
        shutil.move(start, end)