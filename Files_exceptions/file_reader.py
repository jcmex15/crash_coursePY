# Reading an Entire File
# Relative path

# ---------------------------------------------------------------
# with open("Files_exceptions/pi_digits.txt") as file_object:
#     contents = file_object.read()
#     # print(contents)
#     print(contents.rstrip())  # remove the last line
# -------------------------------------------------------------

##  Reading Line by Line

# filename = "Files_exceptions/pi_digits.txt"

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())
# -------------------------------------------------------------

##  Making a List of Lines from a File

# filename = "Files_exceptions/pi_digits.txt"

# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())
# -------------------------------------------------------------
