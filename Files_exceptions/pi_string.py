##  Working with a File’s Contents

# filename = "Files_exceptions/pi_digits.txt"

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ""
# for line in lines:
#     pi_string += line.strip()

# print(pi_string)
# print("len = ", len(pi_string))
# ----------------------------------------------------

## Large Files: One Million Digits

filename = "Files_exceptions/pi_million_digits.txt"

# with open(filename) as file_object:
#     lines = file_object.readlines()

# pi_string = ""
# for line in lines:
#     pi_string += line.strip()

# print(pi_string[:52] + "...")
# print("len = ", len(pi_string))
# ----------------------------------------------------

## Is Your Birthday Contained in Pi?

filename = "Files_exceptions/pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter you birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("You birthday does not appear in the firts million digits of pi.")
# ------------------------------