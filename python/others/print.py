# print numerical value
print(55)

# numerical value can not be started with 0, in maths 055==55 but here it is not, for octal use 0o prefix and 0x for hex 
# print(055) # throws error

# print string 
print("I am string")

# string must be double quoted, so it is error 
# print(This is error bro)

# you can use seperator for print. Anything you print before sep="seperator" will now be seperated by "seperator" overridding the default behaviour of seperation using space. "seperator" is string  for example you want to print date
print(2001,4,22,sep="-") # will be 2001-4-22

# by default, new line ending is added in each print statement, you can override this behaviour using end="end_string", so that "end_string" will be appended after everything in print statement is printed 

print("Khiladi",end="#1") # will now be "Khiladi#1" not "Khiladi\n"
print() # nothing but by default newline

# you can also end with null
print("Ended With Null so no newline",end="\0")
# print()

# you can also specify where to print output, default is sys.stdout, we wil skip this part as not intended for beginners

# specify flush as true or false, if you wanna flush the buffer specified in print statement immediately or later respectively, not for beginners