# Python also allows us to use the else condition for loops. The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

# Python program to demonstrate
# for-else loop

for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break statement is used in for loop and The value of i =",i,"\n")
