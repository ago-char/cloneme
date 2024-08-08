# while loop in python is quit similar to c, you can use break and continue too
"""
syntax:
while condition:
    statements
"""
i = 11
while i > 10:
    if i == 20:
        i += 1
        continue
    print(i)
    i += 1
    if i > 20 and i != 21:
        i += 1
        break
print("..................")
print(i)
