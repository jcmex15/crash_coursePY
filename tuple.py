"""Python refers to values that cannot
change as immutable, and an immutable list is called a tuple"""

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

## Looping Through All Values in a Tuple

elementos = (100,600)
for elemento in elementos:
    print(elemento)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)