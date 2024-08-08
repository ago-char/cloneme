# while with else, else will get executed if while is terminated after full execution not with break
# this will evaluate else as no break used
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")


# this will not evaluate else as break is used
i = 1
while i < 6:
    print(i)
    i += 1
    if i == 6:
        break
else:
    print("i is no longer less than 6")
