def who(jer_num):
    if not isinstance(jer_num, int):
        raise Exception("Passed value to function 'who' must be of 'int' type.")
    elif jer_num == 17:
        return "AB Devillers"
    elif jer_num == 7:
        return "MS Dhoni"
    elif jer_num == 10:
        return "Sachin Tendulkar"
    else:
        return 1


try:
    jersey_num = int(input("Which Number Jersey You Want ? ==> "))
    if isinstance(jersey_num, int):
        if jersey_num == 10 or jersey_num == 17 or jersey_num == 7:
            player = who(jersey_num)
            if isinstance(player, str):
                print(player)
                raise Exception(
                    f"Sorry, Jersey No.{jersey_num} has been retired because it is worn by great {player}."
                )
            else:
                print(f"Congrats, you can have Jersey No.{jersey_num}.")
        else:
            print(f"Congrats, you can have Jersey No.{jersey_num}.")
# how Exception works ? . Actually it is stored in some buffer, if previously and explicitly raised Exception is in top of buffer it will assign it to 'e' you can see 'as e', if not it will print some implicit Exception stored in buffer due to some error in the program or execution
except Exception as e:
    print("Something Unexpected Error : ", e)

print("How is going on")
