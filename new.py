def leet_to_normal(leet_text, leet_dict):
    if not leet_text:
        return [""]
    
    possibilities = []
    for key in leet_dict:
        if leet_text.startswith(key):
            remaining_text = leet_text[len(key):]
            for result in leet_to_normal(remaining_text, leet_dict):
                possibilities.append(leet_dict[key] + result)
    
    if not possibilities:
        return [leet_text[0] + result for result in leet_to_normal(leet_text[1:], leet_dict)]
    
    return possibilities

leet_dict = {
    "uu": "w",
    "ai": "i",
    "i": "1",
    "-|-": "t",
    "|": "L"
}

leet_input = "uuai-|-h"
possible_conversions = leet_to_normal(leet_input, leet_dict)
print("Possible conversions of '{}' into normal text:".format(leet_input))
for conversion in possible_conversions:
    print(conversion)
print("Total number of conversions:", len(possible_conversions))
