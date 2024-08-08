great_players = {17: "AB Devillers", 7: "Ms Dhoni", 10: "Sachin Tendulker"}
jersey_num = 10

try:
    # jersey_num = int(input("Which Number Jersey You Want ? ==> "))
    if isinstance(jersey_num, int):
        if jersey_num in great_players.keys():
            print(great_players[jersey_num])
            raise Exception(
                f"Sorry, Jersey No.{jersey_num} has been retired because it is worn by great."
            )
        else:
            print(f"Congrats, you can have Jersey No.{jersey_num}.")
except Exception as e:
    print(e)
