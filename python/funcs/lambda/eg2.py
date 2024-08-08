# you can even pass variable length args in lambda
x = lambda *args: print(args)
# print(x(5, 9, 22, "sagar"))
x(1, 2, 5)
x(12, 15, 15, 66, 64, 23)
