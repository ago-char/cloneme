string="Ram Giri"

# print the length of string
print(len(string))

# print the whole string
print(string)

# print 4th index of the string 
print(string[4])

# print index 0 through 4
print(string[0:5])

# print index 0 thorugh 4, whenever left pram of [:] is absence, python interpreter itself adds 0 so it be like [0:5]
print(string[:5])

# print the whole string, when ever left pram is absence, interpreter adds 0, and if right is absence it adds len(string) so it will be as such: [0:len(string)], len(string) will be replaced by any calculated numberical value i.e length of string 
print(string[:])

# print the whole string meaning 0 through the end of string as python interpreter adds len(string) to the right parm of [:] it nothing is explicitly defined so it will be like [0:len(string)]
print(string[0:])


# This is how negative indexing works, whenever you specify -n, it will be subtracted from the value yield form len(string), here len(string) returns 12 so [-3:]==[12-3:]==[9:]==[9:12]


# print the last 3 index of string
print(string[-3:])

# print (n-3) to (n-1) index of string 
print(string[-3:-1])

# this does not pring anything as reverse printing is not supported
print(string[4:2]) # but by default in all cases newline is appendeds
