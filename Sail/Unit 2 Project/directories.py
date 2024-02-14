import os


def get_path_depth(path):
    path = os.path.normpath(path)
    return len(path.split(os.sep))


def generate_dir_report(path, report_file_path):
    # Store variable main path depth to know the depth of the provided path.
    main_path_depth = get_path_depth(path)

    # Open the out file for writing.
    with open(report_file_path, "w") as file:

        # Format main path
        formatted_main_path = "+ " + os.path.basename(path)

        # Debug
        print(formatted_main_path)

        # Write main path to file (no indentation)
        file.write(formatted_main_path + "\n")

        # Loop through each
        for root, dirs, files in sorted(os.walk(path)):

            # Calculate directory spacing
            dir_indent = get_path_depth(root) - main_path_depth - 1
            file_indent = dir_indent + 1

            # Debugging..
            # print(f"file indent spacing is {file_indent}")
            # print(f"directory indent spacing is {dir_indent}")

            # Format and record this directory to our output file
            formatted_dir = " " * 2 * dir_indent + "|-+ " + os.path.basename(root)
            print(formatted_dir)
            file.write(formatted_dir + "\n")

            # For all files in this directory format filename and write to file
            for file_name in sorted(files):
                formatted_file_name = " " * 2 * file_indent + "|-- " + file_name
                print(formatted_file_name)
                file.write(formatted_file_name + "\n")


generate_dir_report('data/dir-top', 'dir-report.txt')

"""
Instructions: 


# store variable `main_path_depth` to know what is the depth of the provided path
# open the `out` file for writing
for root, dirs, files in os.walk():
    # store variable `dir_indent` which you can compute as <depth of the root> - `main_path_depth` - 1
    # store variable `file_indent` which you can compute as `dir_indent` + 1
    # write the directory name from the `root` string into the `out` file as a single line; use `dir_indent` to determine prefix and indentation
     for file_name in files:
        # write the `file_name` string into the `out` file as a single line; use `file_indent` to determine prefix and indentation
# close the file explicitly or use the with statement when opening


There are two subtleties you need to deal with.

    The first one is relatively simple. The root variable gives you a path but you only want the name of the directory at the end of the path (reflect on the examples provided above). This can be achieved by calling the os.path.basename function with the path as an argument. See the documentation for details.

    The second subtlety is a bit tricky - you need to figure out what level you are dealing with (top, 1, 2, ...). This will enable you to decide about indentation. This is further complicated by the fact that the path argument may be provided as relative or as absolute. We provide you with the convenience function get_path_depth in the `task4.py file that you will find handy in dealing with this issue. It is up to you how you solve the problem. Our recommendation is to implement the following mapping from levels to indent:

        top-level: -1 (only the directory provided to path will have this level => special case)

        level 1: 0 (directories and files at level 1 do not have any indentation => 0 * 2 spaces)

        level 2: 1 (directories and files at level 2 use two spaces as indentation => 1 * 2 spaces)

        level 3: 2 (directories and files at level 3 use four spaces as indentation => 2 * 2 spaces)

        (etc.)

Do not forget that within each iteration you are writing one line for a directory (coming from root variable) and 0 or more files. The level of the directory is 1 less than that of the files because the files are within that directory. Consider the following:

    iteration 1:

        level -1 (root directory)

        level 0 (files)

    iteration 2:

        level 0 (directory)

        level 1 (files)

    iteration 3:

        level 1 (directory)

        level 2 (files)

Your program should now work like this:



"""

# My output
# + dir-top
# |-+ dir-top
# |-- file1.txt
# |-- file2.txt
# |-+ dir1
#   |-- file3.txt
# |-+ dir2
#   |-- file6.txt
#   |-- file7.log
# |-+ dir3
#   |-- file4.log
#   |-+ dir4
#     |-- file5.txt


# Expected output:
# + dir-top
# |-- file1.txt
# |-- file2.txt
# |-+ dir1
#   |-- file3.txt
# |-+ dir2
#   |-- file6.txt
#   |-- file7.log
# |-+ dir3
#   |-- file4.log
#   |-+ dir4
#     |-- file5.txt


"""
Most recent error from sail... 

[RULE] The `generate_dir_report` function should report the subdirectory structure and the files accurately and follow
| the formatting requirements on leading whitespace and symbols.
[RESULT] FAILED (0/5)
[FEEDBACK] It appears that your implementation of `generate_dir_report` has a mismatch with the reference solution. Your
| implementation reports `|-+ xueofxdaimhcksnvk` at line 31 whereas the reference solution reports `  |-- qvzfkncbcg.mx`.
----------------------------------------------------------------------------------------------------

########################################################################################################################

"""


