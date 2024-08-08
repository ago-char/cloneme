# using for loop when iterable is range 
# define range as range(start,end,inc/dec) where end will not be included i.e ending=end-1
# for ascending order third arg i.e increment is not mandetory but be careful with descending order later 
print("\nWhen range is 1 through 7:")
for i in range(1,8):
    print(i)

print("\nWhen range is 0 through 7:")
for i in range(8):
    print(i)

print("\nWhen range is 1 through 7 with the increment of 2 for each value of i:")
for i in range(1,8,2):
    print(i)

print("\nWhen range is in descending order let;s say form 10 through 1:")
# for reverse order, third arg for range is mandetory. as value are in desc order inc/dec will be on negative. by the way negative increment is actually decrement 
for i in range(10,0,-2):
    print(i)
print()