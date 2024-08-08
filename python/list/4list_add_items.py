# list creation
bfs = ["Yubraj", "Susant", "Pujan"]
gfs = ["BandanaP", "Sadikshya"]
friends = ["Kusal", "Paras"]
newFriends = ["Sugam", "Prabin"]
fbFriends = ["Lie", "SN", "Rahool", "Gary", "Minhaz"]
empty1 = []
empty2 = []
print("\nChange no :", bfs, "\nBoyFriends :", len(bfs))
print("\nChange no :", gfs, "\nGrlFriends :", len(gfs))

# use append method to add at last index without replacing
bfs.append("sagar")
print("\nChange no 1 :", bfs, "\nBoyFriends :", len(bfs))

# use insert to add at the given index without replacing but moving remaining towards right
gfs.insert(1, "Rina")
print("\nChange no 2 :", gfs, "\nGrlFriends :", len(gfs))

# use extend method to extend list with iterable, each element of iterable(string,set,tuple,dict,etc.) will be appened at next new index of existing specified list
print("\nFriends Before :", friends, "\nTotal :", len(friends))
# extend friends with newFriends
friends.extend(newFriends)
print("\nFriends Now :", friends, "\nTotal (after adding newfriends) :", len(friends))

# difference between 'append' and 'extend':
# 'append' will take 1 index at last without replacing
# 'extend' will take len(iterable) index at last placing each element in iterable at last without replacing
print(
    "\nEmpty1 and Empty 2 are empty list as such:\nLen of empty1 :",
    len(empty1),
    "\nLen of empty2 :",
    len(empty2),
)
print("\nEmpty1 :", empty1)
print("\nEmpty2 :", empty2)

print("\nFacebook Friends ", fbFriends, "\nLength :", len(fbFriends))

# appending fbFriends to empty1
empty1.append(fbFriends)
print(
    "\nAppending fbFriends to Empty1, Now Empty1 :", empty1, "\nLength :", len(empty1)
)

# extending empty2 by fbFriends
empty2.extend(fbFriends)
print(
    "\nExtending Empty2 by fbFriends, Now Empty2 :", empty2, "\nLength :", len(empty2)
)
