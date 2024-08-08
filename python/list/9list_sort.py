# by default sort is case sensitive, meaning uppercase are sorted first and then only lowercase which can yeild unexpected result often
f = ["sagar", "Mangal", "anupam", "aNuj", "Zebra"]
print(f)
f.sort()
print(f)

# so better use str.lower or str.upper as key function in sorting
f.sort(key=str.lower)
print(f)

# for reverse sort i.e Z-A
f.sort(reverse=True)
print(f)

# but again this will give unexpected result as key is not set (meaning uppercase first followed by lowercase)
f.sort(key=str.lower, reverse=True)
print(f)

# default is to sort numerically (for numberical values, try mix you'll see error)
n = [10, 5, 49, 55, 22, 24, 15, 100]
n.sort()
print(n)

# set reverse as true if you want in descending order
n.sort(reverse=True)
print(n)

# Note: Make sure you are sorting same data types which can be sorted please
