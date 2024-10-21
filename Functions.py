##Ejemplo
def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()


## Passing Information to a Function
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")


greet_user("jesse")

################################
##### Passing Arguments
#################################


## Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet("hamster", "harry")

## Multiple Function Calls
describe_pet("dog", "willie")

## Keyword Arguments
describe_pet(animal_type="cat", pet_name="corina")


##Default Values
def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name="willie")
describe_pet(pet_name="harry", animal_type="hamster")
print("\n")

##########################
######## Return Values
##########################


## Returning a Simple Value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician, " \n")


## Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
musician = get_formatted_name("john", "hooker", "lee")
print(musician, "\n")


## Returning a Dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    return person


musician = build_person("jimi", "hendrix")
print(musician, "\n")


#### Returning a Dictionary
def build_person(first_name, last_name, age=""):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", age=27)
print(musician, "\n")


## Using a Function with a while Loop
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = first_name + " " + last_name
#     return full_name.title()


# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == "q":
#         break
#     l_name = input("Last name: ")
#     if l_name == "q":
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")


####################
## pasing a list
####################


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)
print("\n")

## Modifying a List in a Function


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
