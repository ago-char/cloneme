car = {"brand": "Ford", "model": "Mustang", "year": 1964}

keys = car.keys()  # return type is dict_keys
values = car.values()  # return type is dict_values
items = car.items()  # return type is dict_items

print("\nBefore The Change :\n")
print(keys, "\n")
print(values, "\n")
print(items, "\n")

car["color"] = "red"
car.pop("year")

# once you track your dictionary using keys,values,items method for dict class, any changes you made will be known to those variables in this case variables are: keys,values,items
print(
    "..........................................................................\n\nAfter The Change i.e. color is added, year is deleted : \n"
)
print(keys, "\n")
print(values, "\n")
print(items, "\n")
