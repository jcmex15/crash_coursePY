"""You’ll be able to store any two kinds of information
that can be matched up, such as a list of words and their meanings, a
list of people’s names and their favorite numbers, a list of mountains and
their elevations, and so forth."""

alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

## Working with Dictionaries
new_points = alien_0["points"]
print("You just earned " + str(new_points) + " points!\n")


## Adding New Key-Value Pairs
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
print("\n")

## Starting with an Empty Dictionary
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)
print("\n")

## Modifying Values in a Dictionary
print("The alien is " + alien_0["color"] + ".")
alien_0["color"] = "yellow"
print("The alien is now " + alien_0["color"] + ".")
print("\n")

## Modifying Values in a Dictionary 2
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original x-position: " + str(alien_0["x_position"]))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0["x_position"] = alien_0["x_position"] + x_increment
print("New x-position: " + str(alien_0["x_position"]))
print("\n")

##Removing Key-Value Pairs
alien_0 = {"color": "green", "points": 5}
print(alien_0)
del alien_0["points"]
print(alien_0)
print("\n")

##A Dictionary of Similar Objects
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("Sarah's favorite language is " + favorite_languages["sarah"].title() + ".")
print("\n")

## Looping Through All Key-Value Pairs
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
for key, value in user_0.items():
    # items() returns a list of key-value pairs.
    print("\nKey: " + key)
    print("Value: " + value)
print("\n")

## Looping Through All Key-Value Pairs 2
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
print("\n")

##Looping Through All the Keys in a Dictionary
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in favorite_languages.keys():
    print(name.title())
print("\n")

for name in favorite_languages.values():
    print(name.title())
print("\n")

## Looping Through All the Keys in a Dictionary2
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(
            " Hi "
            + name.title()
            + ", I see your favorite language is "
            + favorite_languages[name].title()
            + "!"
        )
print("\n")

## Looing Through a Dictionary’s Keys in Order
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
print("\n")
## Looing Through a Dictionary’s Values checking for repeats
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
print("\n")

####################
####  NESTING  #####
####################


## List of Dictionaries (basic)
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print("\n")

## List of Dictionaries (advanced)
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
print("\n")

## List of Dictionaries (advanced_2)
# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(0, 30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print("...")
print("\n")

#############################
#### A List in a Dictionar###
#############################
# Store information about a pizza being ordered.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}
# Summarize the order.
print(
    "You ordered a " + pizza["crust"] + "-crust pizza " + "with the following toppings:"
)
for topping in pizza["toppings"]:
    print("\t" + topping)
print("\n")
## A List in a Dictionar 2
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
print("\n")

####################################
#### A Dictionary in a Dictionary###
####################################
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
