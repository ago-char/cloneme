# dict inside dict is nested dict, dict myFriends contain 3 dict f1,f2,f3 dict inside
friends={
    "f1":{"Name":"Sagar","Home":"Biratnagar"},
    "f2":{"Name":"Shreya","Home":"Damak"},
    "f3":{"Name":"Singam","Home":"Ithari"},
}

# or create 3 dict and add them to new dict 
# create 3 dict 
bro1={
    "Name":"Shiva",
    "Relation":"Elder Brother"
}
bro2={
    "Name":"Ram",
    "Relation":"Second Big Brother"
}
bro3={
    "Name":"Krishna",
    "Relation":"Myself"
}
# add to new dict 
brothers={
    "1st":bro1,
    "2nd":bro2,
    "3rd":bro3
}

# access friends 
N=1
for mainKey in friends:
    print("\nFriend ",N,":\n")
    for key,value in friends[mainKey].items():
        print(key,":",value)
    N+=1
print("\n")

# access brothers 
N=1
for mainKey,nestedDict in brothers.items():
    print("\nBrother ",N,":\n")
    for key_nested in nestedDict:
        print(key_nested,":",nestedDict[key_nested])
    N+=1
print("\n")

# access Name of first brother 
print(brothers["1st"]["Name"])