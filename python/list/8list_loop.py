# let's loop in list

mylove1 = ["Smarika", "Nepal", "Sukrabare", 20, 4.5]
mylove2 = ["Deeya", "Pokheral", "Ramilo", 21, 4.8]
mylove3 = ["Anamika", "Niraula", "Belbari", 19, 4.9]
print("\nMyloves :")
print("..........\n")
# loop through each element
for love in mylove1:
    print(love)
print("..........\n")

# iterate using index
for index in range(0, len(mylove2)):
    print(mylove2[index])
print("..........\n")

# loop with list comprehension
[print(love) for love in mylove3]
print()
