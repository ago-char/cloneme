import time

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
    " ": " ",
}


def leetValuesToString():
    string_leet = ""
    for value in leet_dict.values():
        string_leet += value
    return string_leet


def maximumLenOfValueInLeetDir():
    max_length = 0
    for v in leet_dict.values():
        if len(v) > max_length:
            max_length = len(v)
    return max_length


# if char at given index matches value, then that key will be added to result
# else search_string will give str[from:to+1] to search, if found, it will be added to result
# if not found, str2 will store temporary result i.e combo of result and search string


# at any point of completion search, result will be returned


def findkey(value):
    for key in leet_dict.keys():
        if leet_dict[key] == value:
            return str(key)


def revLeet(text):
    res, sub, i, f, t = "", "", 0, 0, 1
    for k, v in leet_dict.items():
        # print(i)
        if text[i] in leet_dict.values():
            res = res + sub + findkey(text[i])
            f = i + 1
            t += 1
            i += 1
            sub = ""
        else:
            sub = text[f:t]
            if sub in leet_dict.values():
                res = res + findkey(sub)
                sub = ""
                f = t
                t += 1
                i += 1
            else:
                t += 1
                i += 1
        if i == len(text):
            return res + sub


text = input("\nEnter something in Leet Speak to reverse it : ")
print("\nConverting......\n")
time.sleep(2)
print(f"Normal Text should be : {revLeet(text)}\n")
