# any() is a built-in Python function that returns True if at least one element of an iterable (such as a list, tuple, or any other iterable object) evaluates to True. If all elements evaluate to False or if the iterable is empty, any() returns False.
Crushs = ["Anjana", "Smarika", "Deeya"]
check_crush = input("\nWho is Your Crush ? ==> ")
if any(crush.lower() == check_crush.lower() for crush in Crushs):
    print("\n'" + check_crush.capitalize() + "' is your Crush.")
else:
    print("\nYou have Mistaken. Your Crushs are :")
    print(Crushs)
