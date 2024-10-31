## Reading an Entire File

with open("Files_exceptions/pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents)

## Relative path

with open("Files_exceptions/pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())  # remove the last line


## absolute file path

# On Linux and OS X:

# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

# On Windows they look like this:

# file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
# with open(file_path) as file_object:
