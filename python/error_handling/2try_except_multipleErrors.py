l = ["Smarika", "Nepal", "Sukrabare", 20, 4.5]
# index = int(input("Enter index (0-4) to get the value of list 'l' : "))
try:
    index = int(input("What is index ? : "))
    try:
        print(l[index])
    except IndexError:
        print(f"Index Error, {index} is invalid. Valid range is 0 to {len(l)}")
    except ValueError as error:
        print("value error", error)
    except TypeError as error:
        print("Typeerror", error)
except Exception as error:
    print("Some ERROR : ", error)

# index = int(input("ok index : "))
# if isinstance(index, str):
#     print(l[index])
# else:
#     print("ERROR")
