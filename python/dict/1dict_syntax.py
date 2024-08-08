# changable using key
# like this : fav["food"]="salad"

# basic syntax of dictionary is
"""d={
    key1:value1,
    key2:value2,
    ...........
    keyN:valueN
}"""

# comma seperated key value pair can be of any data type where key is represented in string, keys can not be duplicated i.e there can not be more than one key
myfav = {
    "fruit": "mango",  # as no duplicate old is unset
    "fruit": "coconut",  # as no duplicate latest is set
    "numbers": [17, 10, 7],
    "year": 1999,
    "subjects": ["computing", "maths", 10],
}

# validate if fruit is mango or coconut
print(
    myfav["fruit"]
)  # of course it will be "coconut" as assigned latest discarding/overridding old one
# as first key i.e "fruit" is discarded the length of dict myfav will be 4 and not 5
print("The length of dictionay is:", len(myfav))
