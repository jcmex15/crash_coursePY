###########################################
# Doing More Work Within a for Loop
###########################################

magicians = ["alice", "david", "caroline"]
for magician in magicians:
    # print(magician)
    print(magician.title() + ", that was a great tick!")
    print("I cant wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone.That was a great magic show!")

# Making Numeric list
# Range function

for value in range(0, 5):
    print(value)

for value in range(1, 6):
    print(value)

# print even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# print squares numbers
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
