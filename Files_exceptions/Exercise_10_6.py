"""
10-6: Addition
One common problem when prompting for numerical input occurs when people provide text 
instead of numbers. When you try to convert the input to an int, you’ll get a ValueError.
 Write a program that prompts for two numbers. Add them together and print the result. 
 Catch the TypeError if either input value is not a number, and print a friendly error 
 message. Test your program by entering two numbers and then by entering some text 
 .instead of a number.
"""

try:
    x = int(input("give me a number: "))
    y = int(input("give me another number: "))

except ValueError:
    print("Sorry, I really needed a number")

else:
    sum = x+y
    print("The sum of " + str(x)+ " and " + str(y)+ " is "+ str(sum))