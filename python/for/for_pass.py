# The pass statement to write empty loops. Pass is also used for empty control statements, functions, and classes.

letter=5
print("\nValue in letter before loop:",letter,"\n")
# An empty loop
for letter in 'bananas':
    pass
print("Value in letter after loop (well it will be last element of iterable i.e 's' for iterable 'bananas'):",letter,"\n")