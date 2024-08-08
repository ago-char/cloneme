# first create list
friends = [
    "Smarika",
    "Deeya",
    "Deepika",
    "Amrit",
    "Muna",
    "Nirmala",
    "Amrita",
    "Priyanka",
    "Nikita",
    "Neetu",
    "Sunita",
]
print("No change :\n", friends)

# change 3rd friend
friends[2] = "Yunisha"
print("change1 :\n", friends)

# replace 4th friend with 2 friends
friends[3] = ["Shreya", "Simran"]
print("change2 :\n", friends)

# better way to replace is: replace 5th with 3 friends
friends[4:5] = ["Neeru", "Pooja", "Premika"]
print("change3 :\n", friends)
print("Length after 3rd change : ", len(friends), "\n")
# replace all friends except first 2 with one friend
friends[2:] = ["Deepu"]
print("change4 :\n", friends)

# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.
print("Length Now : ", len(friends))

# To insert a new list item, without replacing any of the existing values, we can use the insert() method. The insert() method inserts an item at the specified index:
# place a new friend at the position of 3rd friend, it will not replace 3rd friend, rather make 3rd friend to 4th
friends.insert(2, "Universal Crush")
# if wrong index is given in positive it will insert at last of list and if wrong index is in negative it will insert at beginning
print("This is Last : ", friends, "Length :", len(friends))

# Note : You can do this change using negative indexing too
