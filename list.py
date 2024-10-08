"""
LIST
"""

#######################################
##### accessing elements in a list#####
#######################################

bicycles = ["bike1", "bike2", "bike3", "bike4"]
print(bicycles[0])
print(bicycles[1])
print(bicycles[0].title())

message = "My first bicycle was a " + bicycles[3].title() + "."
print(message)

##################################################
##### changing, adding, and rem oving Elements ###
##################################################

# modifyng elements in a list
motorcycles = ["motorbike1", "motorbike2", "motorbike3"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

# adding elemnts to a list
motorcycles.append("zuzuki")
print(motorcycles)

# Make easy a dynamic list
motorcycles1 = []
motorcycles1.append("1")
motorcycles1.append("2")
motorcycles1.append("3")
print(motorcycles1)

# inserting elements into a list
motorcycles = ["motorbike1", "motorbike2", "motorbike3"]
motorcycles.insert(0, "ducati")
print(motorcycles)

# removing elemnts from a list
motorcycles = ["motorbike1", "motorbike2", "motorbike3"]
del motorcycles[0]
print(motorcycles)

# removing using pop() Method
print("###")
motorcycles = ["motorbike1", "motorbike2", "motorbike3"]
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# removing an item by value
print("###")
motorcycles = ["motorbike1", "motorbike2", "motorbike3"]
motorcycles.remove("motorbike1")
print(motorcycles)

# remove() method working with a value
print("###")
motorcycles = ["motorbike1", "motorbike2", "motorbike3"]
too_expensive = "motorbike3"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is to expensive for me. \n")
print
#######################################
##### Organizing a list #####
#######################################

# Sorting a List Permanently with the sort(), sorted

cars = ["bmw", "audi", "toyota", "subaru"]
# cars.sort()
# cars.sort(reverse=True)
print(cars)
print("\nHere is the original list:")
print(cars)

print("\nHere is the original list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
print("\n")
cars.reverse()
print(cars)

# length of alist

print(len(cars))
print("\n")

# Access to the last index
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles[-1])

################################################
### Making Numerical Lists
################################################

for value in range(1,5):
    print(value)

#### Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

#### Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

### even numbers 
even_numbers = list(range(2,11,2))
print(even_numbers)

### square numbers
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

## List Comprehensions
squares = [value**2 for value in range (1,11)]
print(squares)

###################################################
########### Working with Part of a List
##################################################

## Slicing a List
players = ['charles','martina','michel','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

## Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

## Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('caneloni')
friend_foods.append('ice cream')

print("My favorite foods are")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
