# use update method for dict class object to change the value of existing key of dict 
# create dictionary 
mydict={
    "quickNap":10,
    "jhutti_cut":"impossible_short",
    "kadak":"unbelievable",
    "cricket":["ABD","MSD","BOSS"],
    "football":"Leonal Messi"
}

# use of update method 
print("\nValue for Key 'kadak' before :",mydict["kadak"],"\n")
mydict.update({"kadak":"badiya"})
print("Value for Key 'kadak' after  :",mydict["kadak"],"\n")

# update value for multiple keys or even add new key:value, here "bhalu":"bear" key value is added and other 2 are updated. The difference is when you add new key:value pair using update method, code editors like: vs code may not give suggestion for the keys added using update method
mydict.update({"quickNap":20,"jhutti_cut":"can't repeat","bhalu":"bear"})
print("English for 'bhalu' is",mydict["bhalu"]+".\n")
print("Taking quickNap of",mydict["quickNap"],"minutes.\n")

print("Football before :",mydict["football"])
# you can change the value for key using indexing 
mydict["football"]="LM10"
print("Football now    :",mydict["football"],"\nSomeone who is permanent in my heart.\n")