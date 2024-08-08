# for loop where iterable is dict
car = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}

# car.items() will get key and value which are then stored in k and v iterating through the end of car

for k, v in car.items():
    print(k, ":", v)

print("...............")

# car.keys() will get key of dict and they will now be iterable
for k in car.keys():
    print(k, end=" ")

print("\n..............")

# car.keys() will get key of dict and they will now be iterable

for v in car.values():
    print(v, end=" ")

print()
