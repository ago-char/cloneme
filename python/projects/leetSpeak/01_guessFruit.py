fruits = [
    "apple",
    "mango",
    "orange",
    "banana",
    "pear",
    "pineapple",
    "graves",
    "guava",
    "litchi",
    "watermelon",
    "strawberry",
    "avocado",
    "blueberry",
]
print(len(fruits))
counter = 1
for f in fruits:
    print("Hint : ", f[0] + "_____" + f[-1], "\n")
    if input("Your Guess : ").casefold() == f.casefold():
        print("You Won !!...Next Level\n")
        counter += 1
        continue
    else:
        if counter == len(fruits):
            print("\nEnd...Try after Few Moments\n")
            break
        print("Hard Luck, Try Next...\n")
        counter += 1
