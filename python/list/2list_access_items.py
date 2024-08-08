# create list
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# as list are indexed (starting from 0), they are accessed using index
print("Fruit Number 5 :", fruits[4])

# access using negative index, whenever negative index are there, they are meant to get subtracted from the length of list, suppose you see following: fruits[-1] i.e fruits[len(fruits)-1] = fruits[7-1] which is as good as fruits[6], so if you wanna access list from last you will start with -1,-2,-3,-4,-5,-6,-7 i.e -1 througn -len(list)
print("Fruit at last index : ", fruits[-1])

# access using range
# fruits[i:j] # from 'i' to 'j-1'
# fruits[:j] # from '0' to 'j-1'
# fruits[:] # from '0' to 'j-1'
# fruits[i:] # from '0' to 'j-1'
# fruits[i:j:k] # from 'i' to 'j' with the increment of 'k'
# fruits[j:i:-k] # from 'j' to 'i' with the decrement of 'k'
# if 'i' and 'j' are ommitted while 'k' is positive that will be from 0th index to last index.
# if 'j' and 'i' are ommitted while 'k' is negative that will be from last index to 0th index.
# you can also use negative indexing, the interpretation of negative indexing is already described at line 7. Ranges in negative index are such if 'i' and/or 'j' are prefixed with '-' (minus sign)

print("Fruit first to Last :", fruits[::])
print("Fruit last to first :", fruits[::-1])

if "mango" in fruits:
    print("\nMango Index : ", fruits.index("mango"))
else:
    print("\nMango is not in the list of fruits we have\n")
