# use of continue statement in for loop 

# Prints all letters except 'e' and 's'
for letter in 'greenbeautifulsarenotroses':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

# as 's' can not be printed inside loop last letter 's' is skipped by continue statement, letter will still have its value i.e 's' 
print("Current letter after loop ends :",letter)
