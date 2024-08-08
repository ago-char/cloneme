# use of lambda inside function (sort of func returning func(lambda ofc))
def myfunc(n):
    return lambda x: x**n


# myfunc is called and return of myfunc i.e 'lambda x:x**n' which is basically function is returned, is stored on 'var'
var = myfunc(5)  # so var is actually 'lambda x:x**n'
# pass 'some_num' to var and it will return 'some_num' to the power 'n', var has the copy of 'n' which value is 5
print(var(4))
print(4**5)
