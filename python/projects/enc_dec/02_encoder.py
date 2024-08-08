# encode string append first char to the rest string and add random 4 chars at the beginning and random 4 chars at the end

import random
import string


def encoder_len():
    return 10


plaintext = input("Enter Password, It will be encoded : ")
encoded_string = plaintext.removeprefix(plaintext[0]) + plaintext[0]


for rand in range(encoder_len()):
    encoded_string = (
        random.choice(string.ascii_letters)
        + encoded_string
        + random.choice(string.ascii_letters)
    )

print(encoded_string)
