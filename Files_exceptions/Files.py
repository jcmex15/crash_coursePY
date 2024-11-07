#############################
## Reading an Entire File ###
#############################

with open("Files_exceptions/pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents)
#--------------------------------------------------------------------------------    

#############################
## Relative path ############
#############################

with open("Files_exceptions/pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())  # remove the last line
#---------------------------------------------------------------------------

#############################
## absolute file path  ######
#############################
# On Linux and OS X:

# file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
# with open(file_path) as file_object:

# On Windows they look like this:

# file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
# with open(file_path) as file_object:
#--------------------------------------------------------------------------

###########################
###### Writing to a File ##
###########################

# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.")
#----------------------------------------------------------------------

#####################
## Storing Data #####
####################


"""
The JSON (JavaScript Object Notation) format was originally developed for JavaScript.
However, it has since become a common format used by many languages, including
Python.
"""