"""
10-7: Addition Calculator
Wrap your code from Exercise 10-6 in a while loop so the user can continue entering 
numbers even if they make a mistake and enter text instead of a number.
"""

print("Enter 'q' at any time to quit.\n")

while True:

    try:
        x = input("give me a number: ")
        if x == 'q':
            break
        x = int(x)

        y = input("give me another number: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number")

    else:
        sum = x+y
        print("The sum of " + str(x)+ " and " + str(y)+ " is "+ str(sum))