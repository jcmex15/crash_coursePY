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
