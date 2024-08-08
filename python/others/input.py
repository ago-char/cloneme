# input function is used to interact with users to take user data. by default whatever user entered is returned as string, so we need to typecast if necessary. Input function takes string as argument (which is optional). Any string you pass to this function will be displayed in stdout. This helps to give user some info about expected input

name=input("FirstName: ")
num=int(input("Enter a number to find its square : "))
print(name.split(' ',1)[0],end="\0")
print(", The square of",num,"is",num**2,".")
