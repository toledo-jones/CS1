import os
from pathlib import Path


def generate_dir_report(path,
                        report_file_path,
                        show_files,
                        num_files,
                        file_size,
                        hl):

    # store variable `main_path_depth` to know what is the depth of the provided path
    # open the `out` file for writing
    for root, dirs, files in os.walk(path):
    # store variable `dir_indent` which you can compute as <depth of the root> - `main_path_depth` - 1
    # store variable `file_indent` which you can compute as `dir_indent` + 1
    # write the directory name from the `root` string into the `out` file as a single line; use `dir_indent` to determine prefix and indentation
     for file_name in files:
        # write the `file_name` string into the `out` file as a single line; use `file_indent` to determine prefix and indentation
    # close the file explicitly or use the with statement when opening

generate_dir_report('data/dir-top', 'dir-report.txt')
