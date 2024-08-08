# create dict 
mycom={
    "CPU":"Ryzon5",
    "HDD":"1 TB",
    "RAM":"16 GB",
    "GPU":"GEFORCE GTX",
    "Nested Virtualization":False,
    "Fans":2,
    "WiFi_Adapter":2
}

print()
print(mycom,"\n")
# fans were removed as computer is not being use for complex process and even not for long time 
# use pop method for deleting
mycom.pop("Fans")
print("Fans were removed\n",mycom,"\n")

# fans installed again but this time only 1 
mycom.update({"Fans":1})
print("Fans added again but 1\n",mycom,"\n")

# popitem method removes last inserted item form dict, in this case it will be Fans. If no insertion was made after the creation of dict, last added item at the time of creation will get deleted as simple as that 
mycom.popitem()
print("Fans removed again as no Heating was observed\n",mycom,"\n")

# Latest version wireless Wi-Fi Adapters were thieved, use del keyword followed by key index to del particular key
del mycom["WiFi_Adapter"]
print("Wifi Adapters were taken by thug\n",mycom,"\n")

# computer was destroyed by overload and no items were recovered so better clear mycom but not delete entire dict because we are in plan of purchasing new 
mycom.clear()
print("No components Left")
print(mycom,"\n")

# plan of purchasing computer is posponed to unknown time so better delete entire dict now 
del mycom
print("Get Ready For Error :\n")
print(mycom) # will throw error as mycom no longer exist