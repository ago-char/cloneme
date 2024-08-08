def scanInt(displayMessage="", verbose=False):
    """
    Return inputted 'int' if you provide 'int' convertable value in stdin, else return none. You can check return type for further easyness in your code/program.
    Pass 'True' if you want verbose Message, else 'False' to verbose. Default is 'False'

    use this function if you want your code do not stop because of the value error, if you use just input then to typecast it to int, if the value user provides is not convertable to int, your program will stop there. This is not the case here.
    """
    x = 4
    try:
        # x = int(input(displayMessage))
        x = input(displayMessage)
        x = int(x)
        return x
    except:
        if verbose == True:
            print(
                f"Expected Value is of <class 'int'>. You entered '{x}' which is of {type(x)}. Just Does not Fit the case."
            )


def keepAskingInt(displayMessage="Give me a NUMBER ==> ", verbose=False):
    """
    This is just a recursice version of 'scanInt()'. It will keep asking the user to enter a number until he provides one. Pass 'True' if you want verbose Message, else 'False' to verbose. Default is 'False'
    """
    num = scanInt(displayMessage, verbose)
    while True:
        if not isinstance(num, int):
            num = keepAskingInt(displayMessage, verbose)
        else:
            return num


def onlyInt():
    print("You are on onlyInt")
