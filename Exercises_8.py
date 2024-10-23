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


print(city_country("santiago", "chile"), "\n")

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


# def make_album(artist, title, tracks=0):
#     # create diccionary
#     album_dict = {"artist": artist.title(), "title": title.title()}
#     if tracks:  # si existen tracks, entonces
#         album_dict["tracks"] = tracks
#     return album_dict


# # prepare the prompts
# title_prompt = "\nWhat album are you thinking of? "
# artist_prompt = "Who's the artist "

# # Let the user know how to quit.

# print("Enter 'quit' at any time to stop")

# while True:
#     title = input(title_prompt)
#     if title == "quit":
#         break

#     artist = input(artist_prompt)
#     if artist == "quit":
#         break

#     album = make_album(artist, title)
#     print(album)

# print("\nThanks for responding!")

"""
8-9: Magicians
Make a list of magician’s names. Pass the list to a function 
called show_magicians(), wich prints the name of each magician 
in the list.
"""


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


magicians = ["harry houdini", "harry poter", "sabrina spellman"]
show_magicians(magicians)
print("\n")

"""
8-10: Great Magicians
Start with a copy of your program from Exercise 8-9. Write a function called make_great() 
that modifies the list of magicians by adding the phrase the Great to each magician’s name.
Call show_magicians() to see that the list has actually been modified.
"""


def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)


def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + " the Great"
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians = ["Harry Houdini", "David Blaine", "Teller"]
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)
print("\n")


"""
8-12: Sandwiches
Write a function that accepts a list of items a person wants on a sandwich. The function should 
have one parameter that collects as many items as the function call provides, and it should 
print a summary of the sandiwch that is being ordered. Call the function three tiems, using a 
different number of arguments each time
"""


def make_sandwich(*items):
    for item in items:
        print("......adding " + item + " to yopur sandwich")
    print("your sandwich is ready")
    print("\n")


make_sandwich("roast beef", "cheddar cheese", "lettuce", "honey dijon")

make_sandwich("turkey", "apple slices", "honey mustard")
make_sandwich("peanut butter", "strawberry jam")

"""
8-14: Cars
Write a function that stores information about a car in a dictionary. the function should 
always receive a manufacturer and a model name. It should then accept an arbitrary number
of keyword arguments. Call the function with the required information and two other name-value.
pairs, such as a color or an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that’s returned to make sure all the information was stored correctly
"""


def make_car(manufacturer, model, **options):
    # definir diccionario
    car_dict = {"manufaturer": manufacturer.title(), "model": model.title()}
    for option, value in options.items():
        car_dict[option] = value

    return car_dict


print(make_car("subaru", "outback", color="blue", tow_package=True))


print(make_car("honda", "accord", year=1991, color="white", headlights="popup"))
print(make_car("honda", "accord"))
