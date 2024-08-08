# set joining operations
# update() -- eg. s1.update(s2,s3)   (no return)
# union () -- | eg. s4=s1.union(s2,s3) i.e s4=s1|s2|s3 (return)
# intersection_update() -- (no return)
# intersection() -- & (return) s4=s1 & s2 & s3
# difference_update() -- (no return)
# difference -- use - operator (return) eg: s1=s2-s3
# symmetric_difference_update() -- (no return)
# symmetric_difference() -- use ^ operator (return)


s1 = {1, 3, 5, 7, 9, 10}
s2 = {2, 4, 6, 8, 10}
s3 = {12, 14, 16, 18, 20, 10}

# join s2 and s3 so that s2 will have all the elements of s3, update method will do so, add set in existing set
print(s2)
s2.update(s3)
print(s2)
print(type(s2))

print("............................\n")

# if you want s4 so as the result on joining s1 and s3 you can not use update as it won't return anyting so use union method. It will not update any sets (the caller set and the argc set), rather it returns union of those 2 set
s4 = s1.union(s3)
print(s1)
print(s3)
print(s4)

print("............................\n")
# intersection method will return duplicate only
print(s1.intersection(s2, s3))  # {10} is common in all 3
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

print("............................\n")

# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersecton() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set1)
print(set3)

print("............................\n")

# difference vs symmitric difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2  # difference
print(set3)
set3 = set1 ^ set2  # symmitric difference (a-b|b-a)
print(set3)
print(set1 - set2 | set2 - set1)  # symmitric difference (a-b|b-a)
