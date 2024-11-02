"""
10-1: Learning Python
Open a blank file in your text editor and write a few lines summarizing 
what you've learned about Python so far. Start each line with the phrase 
In Python you can... Save the file as learning_python.txt in the same 
directory as your exercises from this chapter. Write a program that 
reads the file and prints what you wrote two times: print the contents
once by reading in the entire file, and once by storing the lines in 
a list and then looping over each line.
"""

from pathlib import Path

print("--- Reading in the entire file:")
path = Path("learning_python.txt")
contents = path.read_text()
print(contents, "\n")

print("--- Looping over the lines:")
lines = contents.splitlines()
for line in lines:
    print(line)
print("\n")

"""
10-2: Learning C
You can use the replace() method to replace any word in a string with a different word. 
Here's a quick example showing how to replace 'dog' with 'cat' in a sentence:

>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'

Read in each line from the file you just created, learning_python.txt, and replace 
the word Python with the name of another language, such as C. Print each modified line 
to the screen.
"""

from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace("Python", "C")
    print(line)
print('\n')