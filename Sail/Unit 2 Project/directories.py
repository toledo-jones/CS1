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
        level = -1
        # Loop through each
        for root, dirs, files in sorted(os.walk(path)):


            # Calculate directory spacing
            dir_indent = get_path_depth(root) - main_path_depth - 1
            file_indent = dir_indent + 1

            # Debugging..
            # print(f"file indent spacing is {file_indent}")
            # print(f"directory indent spacing is {dir_indent}")

            # Format and record this directory to our output file
            if level > -1:
                formatted_dir = " " * 2 * dir_indent + "|-+ " + os.path.basename(root)
                print(formatted_dir)
                file.write(formatted_dir + "\n")

            # For all files in this directory format filename and write to file
            for file_name in sorted(files):
                formatted_file_name = " " * 2 * file_indent + "|-- " + file_name
                print(formatted_file_name)
                file.write(formatted_file_name + "\n")
            level += 1


generate_dir_report('data/dir-top', 'dir-report.txt')

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


