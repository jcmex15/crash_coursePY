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
