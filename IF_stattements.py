cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

## Checking Whether a Value Is Not in a List
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
