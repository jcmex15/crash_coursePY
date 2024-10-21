"""8-1: Message
Write a function called display_message() that prints
 one sentence telling everyone what you are learning 
 about in this chapter. Call the function, 
 and make sure the message displays correctly."""


def dispaly_message():
    msg = "I'm learning to store code in functions."
    print(msg)


dispaly_message()
print("\n")

"""8-2: Favorite Book
Write a function called favorite_book() that accepts 
one parameter, title. The function should print a message,
 such as One of my favorite books is Alice in Wonderland.
Call the function, making sure to include a
book title as an argument in the function call."""


def favorite_book(title):
    print(f"{title} is one of my favorite books", "\n")


favorite_book("Viaje al centro de la tierra")

"""8-3: T-Shirt
Write a function called make_shirt() that accepts
 a size and the text of a message that should be printed
on the shirt. The function should print a sentence 
summarizing the size of the shirt and the message printed
on it.

Call the function once using positional arguments 
to make a shirt. Call the function a second time 
using keyword arguments."""


def make_shirt(size, message):
    print(f"\nI'm going to make {size} tshirt")
    print(f"It will say, {message}\n")


make_shirt("M", "Viva Mexico")

"""8-4: Large Shirts
Modify the make_shirt() function so that shirts are 
large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default 
message, and a shirt of any size with a different message."""


def make_shirt(size="large", message="I love python"):
    print(f"\nI'm going to make {size} tshirt")
    print(f"It will say, {message}\n")


make_shirt()
make_shirt(size="M")
make_shirt(message="I love Mexico")

"""8-5: Cities
Write a function called describe_city() that accepts the name
 of a city and its country. The function should print a 
 simple sentence, such as Reykjavik is in Iceland. 
 Give the parameter for the country a default value. 
 Call your function for three different cities, 
 at least one of which is not in the default country."""


def describe_city(city, country="Colombia"):
    print(f"{city.title()} is in {country.title()}\n")


describe_city("Pereira")
describe_city("santiago", "chile")
describe_city("puerto vallarta")

"""8-6: City Names
Write a function called city_country() that takes in the name
of a city and its country. The function should return
 a string formatted like this:

“Santiago, Chile”

Call your function with at least three city-country pairs, 
and print the value that’s returned."""


def city_country(city, country):
    return f"{city.title()}, {country.title()}"


print(city_country("santiago", "chile"))

"""8-7: Album
Write a function called make_album() that builds a dictionary 
describing a music album. The function should take in an 
artist name and an album title, and it should return a 
dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing 
different albums. Print each return value to show that the 
dictionaries are storing the album information correctly.

Add an optional parameter to make_album() that allows you 
to store the nubmer of tracks on an album. If the calling 
line includes a value for the number of tracks, add that 
value to the album’s dictionary. Make at least one new 
function call that includes the nubmer of tracks on an album."""
