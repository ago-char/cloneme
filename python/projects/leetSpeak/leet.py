leet_dict = {
    "a": "4",
    "A": "/-\\",
    "b": "b",
    "B": "l3",
    "c": "c",
    "C": "(",
    "d": "d",
    "D": "])",
    "e": "3",
    "E": "3",
    "f": "f",
    "F": "|#",
    "g": "9",
    "G": "(_+",
    "h": "h",
    "H": "|-|",
    "i": "ai",
    "I": "|",
    "j": "j",
    "J": "_)",
    "k": "k",
    "K": "]{",
    "l": "`1",
    "L": "|_",
    "m": "m",
    "M": "/\\/\\",
    "o": "0",
    "O": "()",
    "p": "p",
    "P": "|*",
    "q": "q",
    "Q": "()_",
    "r": "r",
    "R": "|2",
    "s": "5",
    "S": "$",
    "t": "-|-",
    "T": "7",
    "u": "(_)",
    "U": "|_|",
    "v": "v",
    "V": "\\/",
    "w": "uu",
    "W": "\\/\\/",
    "x": "*",
    "X": "><",
    "y": "`)",
    "Y": "`/",
    "z": ">_",
    "Z": "7_",
}


def leetOf(string, mode):
    result = ""
    operational_char = ""
    if type(string) is str and type(mode) is int:
        for char in string:
            if mode == 1:
                operational_char = char.lower()
            elif mode == 2:
                operational_char = char.upper()
            else:
                operational_char = char
            if operational_char in leet_dict.keys():
                result += leet_dict[operational_char]
            else:
                result += operational_char
    return result


user_input = input("Text to LeetSpeak : ")
print("Original Mode = ", leetOf(user_input, 1))
print("Classic  Mode = ", leetOf(user_input, 3))
print("Ultra    Mode = ", leetOf(user_input, 2))
