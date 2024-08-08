def fact(num):
    """
    Usuage: fact(num)

    where num is <class 'int'> type

    Returns : <class 'int'> factorial of 'num'
    """
    if num == 0 or num == 1:
        return 1
    return num * fact(num - 1)


n = int(input("Enter a number to calculate Factorial : "))
print(f"Factorial of {n} is {fact(n)}.")
