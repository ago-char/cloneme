# demonstrating match case (switch case in c/cpp. the difference is that break; statement is not required. it is only for loop)
# as of python 3.10 it has been added, earlier version of python does not have this match_case 
n=22
m=22
match n:
    #  if the value of n is 11 
    case 11:
        print("case11")
    # if the value of n is 55 
    case 55:
        if m<40:
            print(m,"< 40")
        else:
            print(m,">= 40")
    # if m is 22 and n should be equal to m 
    case 22 if m==n:
            print("m and n are equal, as: ",m,n)
    # default case means when no cases are hit
    case _:
        print("Default Case: ",m)

print("\nDone")