"""
10-8: Cats and Dogs
Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first 
3file and three names of dogs in the second file. Write a program that tries to read 
these files and print the contents of the file to the screen. Wrap your code ina 
try-except block to catch the FileNotFound error, and print a friendly message if a 
file is missing. Move one of the files to a different location on your system, and 
make sure the code in the except block executes properly.
"""

# filenames=['Files_exceptions/cats.txt','Files_exceptions/dogs.txt']

# for filename in filenames:
#     print('\nReadin file: '+ filename)

#     try:
#         with open(filename) as f:
#             contents = f.read()
#             print(contents)
    
#     except FileNotFoundError:
#         print(" Sorry, I cant find that file")

#-----------------------------------------------------------------

## Modify your except block in Exercise 10-8 to fail silently if either file is missing.

filenames=['Files_exceptions/cats.txt','Files_exceptions/dogs.txt']

for filename in filenames:
    
    try:
        with open(filename) as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        print("\nReading file: " + filename)
        print(contents)