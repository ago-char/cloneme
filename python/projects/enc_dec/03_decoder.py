import string
import random


def encoder_len():
    return 10


encoded_string = input("Enter Encoded Message to Decode : ")
decoded_string = encoded_string
length = len(encoded_string)
if length > 0:
    for i in range(encoder_len()):
        decoded_string = decoded_string.removeprefix(decoded_string[0])
        decoded_string = decoded_string.removesuffix(decoded_string[-1])
    last_char = decoded_string[-1]
    decoded_string = decoded_string.removesuffix(last_char)
    decoded_string = last_char + decoded_string
    print(decoded_string)
else:
    print("Invalid Input Detected...")
