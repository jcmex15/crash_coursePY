"""
9-1: Restaurant
Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a 
cuisine_type. Make a method called describe_restaurant() that 
prints these two pieces of information, and a method called 
open_restaurant() that prints a message indicating that the 
restaurant is open.

Make an instance called restaurant from your class. 
Print the two attributes individually, and then call 
both methods."""


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\n" + self.name + " serves wonderful " + self.cuisine_type)

    def open_restaurant(self):
        print("\n" + self.name + " is opnen. Comeo on in!")


restaurant = Restaurant("the mean queen", "pizza")
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")

"""
9-3: Users
Make a class called User. Create two attributes called first_name 
and last_name, and then create several other attributes that are 
typically stored in a user profile. Make a method called 
describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized 
greeting to the user.

Create several instances representing different users, and call 
both methods for each user.
"""


class User:
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Username" + self.username)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")


eric = User("eric", "matthes", "e_matthes")
eric.describe_user()

"""
9-4: Number Served
Start with your program from Exercise 9-1 (page 166). Add an 
attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, 
and then change this value and print it again.

Add a method called set_number_served() that lets you set 
the number of customers that have been served. Call this 
method with a new number and print the value again.

Add a method called increment_number_served() that lets you 
increment the number of customers who’ve been served. Call 
this method with any number you like that could represent 
how many customers were served in, say, a day of business.
"""


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\n" + self.name + " serves wonderful " + self.cuisine_type)

    def open_restaurant(self):
        print("\n" + self.name + " is opnen. Comeo on in!")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


restaurant = Restaurant("the mean queen", "pizza")
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))

restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))
print("\n")

"""
9-5: Login Attempts
Add an attribute called login_attempts to your User class 
from Exercise 9-3 (page 166). Write a mehtod called 
increment_login_attempts() that increments the value of 
login_attempts by 1. Write another method called 
reset_login_attempts() that resets the value of 
login_attempts to 0.

Make an instance of the User class and call 
increment_login_attempts() several times. Print the value 
of login_attempts to make sure it was incremented properly, 
and then call reset_login_attempts(). Print login_attempts 
again to make sure it was reset to 0.
"""


class User:
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("Username" + self.username)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """increments the value of login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """that resets the value of login_attempts to 0"""
        self.login_attempts = 0


eric = User("eric", "matthes", "e_matthes")
eric.describe_user()

print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))

print("Resetting login attempts...")
eric.reset_login_attempts()
print("  Login attempts: " + str(eric.login_attempts))

"""
9-14: Dice
The module random contains functions that generate random 
numbers in a variety of ways. The function randint() returns 
an integer in the range you provide. the following code 
returns a number between 1 and 6:

from random import randint
x = randint(1, 6)

Make a class Die with one attribute called sides, which has 
a default value of 6. Write a method called roll_die() that 
prints a random number between 1 and the number of sides 
the die has. Make a 6-sided die and roll it 10 times.

Make a 10-sided die and a 20-sided die. Roll each die 10 times
"""

from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results, "\n")
