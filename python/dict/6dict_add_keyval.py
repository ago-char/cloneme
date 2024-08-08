# adding is same as updating 
# create new dictionary 
mycom={
    "CPU":"Ryzon5",
    "HDD":"1 TB",
    "RAM":"16 GB",
    "GPU":"GEFORCE GTX",
    "Nested Virtualization":False
}

print() # nothing meaning new line only 
print(mycom,"\n")
# new SDD is installed 
mycom["SDD"]="512 GB"
print(mycom,"\n")
# fans are added 
mycom.update({"fans":2})
print(mycom,"\n")
