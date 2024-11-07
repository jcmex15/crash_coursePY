##########################
###### Exceptions  #####
##########################

""""
If you write code
that handles the exception, the program will continue running. If you don’t
handle the exception, the program will halt and show a traceback, which
includes a report of the exception that was raised.
Exceptions are handled with try-except blocks. A try-except block asks
Python to do something, but it also tells Python what to do if an exception
is raised. When you use try-except blocks, your programs will continue
running even if things start to go wrong
"""

#print(5/0)

## Using try-except Blocks

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("\nYou can't divide by zero!\n")
#----------------------------------------------------

## Using Exceptions to Prevent Crashes

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number =input("\nFirst number: ")
#     if first_number =='q':
#         break
#     second_number =input("\nSecond number: ")
#     if second_number =='q':
#         break
# answer = int(first_number) / int(second_number)
# print(answer)
# --------------------------------------------------------

## The else Block

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number =input("\nFirst number: ")
#     if first_number =='q':
#         break
#     second_number =input("\nSecond number: ")
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by o!")
#     else:
#         print(answer)
    # --------------------------------------------------------

## Handling the FileNotFoundError Exception

# """
# Let’s try to read a file that doesn’t exist. The following program tries
# to read in the contents of Alice in Wonderland, but I haven’t saved the file
# alice.txt in the same directory as alice.py:
# """

# filename = "alice"

# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
#     print(contents)
# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist"
#     print(msg)
# ----------------------------------------------------------------------------

##  Analyzing Text

## The split() method
# tittle = "Alice in wonderland"
# print(tittle.split())

# filename = 'Files_exceptions/alice.txt'

# try:
#     with open(filename) as file_object:
#         contents = file_object.read()
#     #print(contents)
# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist"
#     print(msg)
# else:
#     # Count the approximate number of words in the file.
#     words = contents.split()
#     num_words = len(words)
#     print("The file " + filename + " has about " + str(num_words) + " words.")
#------------------------------------------------------------------------------    

##  Working with Multiple Files

# def count_words(filename):
#     """Count the approximate number of words in a file."""
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         msg = "Sorry, the file " + filename + " does not exist."
#         print(msg)
#     else:
#         # Count approximate number of words in the file.
#         words = contents.split()
#         num_words = len(words)
#         print("The file " + filename + " has about " + str(num_words) +
#             " words.")
    
# # filename ='Files_exceptions/alice.txt'
# # count_words(filename)

# filenames = ['Files_exceptions/alice.txt', 'Files_exceptions/siddhartha.txt', 
# 'Files_exceptions/moby_dick.txt', 'Files_exceptions/little_women.txt']
# for filename in filenames:
#     count_words(filename)
#------------------------------------------------------------------------------

##  Failing Silently