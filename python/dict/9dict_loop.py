# loop in dict 
person1={
    "Name":"Hari Bahadur",
    "Age":34,
    "Height":5.3,
    "Religion":"Hindu",
    "Ethnicity":"Chhetri",
    "Location":"Biratnagar"
}

print("..................................................................\nLoop through Keys :\n")
for key in person1:
  print(key)

print("..................................................................\nLoop through Keys but print Values using those Keys :\n")
for key in person1:
  print(person1[key])  # can use person1.get[x] use get method

print(".................................................................\nLoop through Keys using 'keys' method :\n")
for key in person1.keys():
  print(key)

print(".................................................................\nLoop through Values using 'values' method :\n")
for value in person1.values():
  print(value)

print(".................................................................\nLoop through both Keys and Values, by using the 'items' method :\n")
for key, value in person1.items():
  print(key,":", value)
print() # leave empty line at last 