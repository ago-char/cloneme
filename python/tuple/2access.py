t = "smarika", "deeya", "deepu"  # this is tuple

# tuple are accessed using index
print(t[2])

# negative indexing works too
# range of index works too

# tuple from first to last
print(t[:])
# tuple from last to first
print(t[::-1])

# check if item exists on tuple
x = input("Enter your Crush Name : ")
if x in t:  # checking
    print(x + " is your crush.\n")
else:
    print(x + " is not your crush bro.")
    print("Your Crushes :", t)
