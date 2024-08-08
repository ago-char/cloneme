# create dictionay
mydict = {
    "quickNap": 10,
    "jhutti_cut": "impossible_short",
    "kadak": "unbelievable",
    "cricket": ["ABD", "MSD", "BOSS"],
}

# access using key
print(
    "\nAccessing values of dict using its key, The value for key 'quickNap' is :",
    mydict["quickNap"],
    "\n",
)

# using get method for class dict
print(
    "Accessing value using get() method as such -- mydict.get(\"kadak\") for key 'kadak' is :",
    mydict.get("kadak"),
    "\n",
)

# if you want all keys be in seperate list you can use keys method for the class dict, resulting object will be of class named <class 'dict_keys'>
key_list = mydict.keys()
print(
    "Using keys() method to get list of keys in 'mydict' -- mydict.keys() and They are: "
)
print(key_list, "\n")

# however you can not access each item in the list so better use list function to convert into list. Meaning that : resulting type 'dist_keys' is immutable and can't be accessed using index, you can still loop though.
print(
    "However you can not access each item in the list ( as resulted list is not of class list, it is of <class 'dict_keys'> ) so better use list function to convert into list \n"
)
k_list_mydict = list(mydict)  # same result if list(mydict.keys())
print("First Key -- k_list_mydict[0] is :", k_list_mydict[0], "\n")
