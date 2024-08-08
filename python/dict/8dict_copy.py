mydict={
    "quickNap":10,
    "jhutti_cut":"impossible_short",
    "kadak":"unbelievable",
    "cricket":["ABD","MSD","BOSS"]
}

# copy just like assignment 
x=mydict

# better use dict function to typecast 
y=dict(mydict)

# better use copy method for dict to copy
z=mydict.copy()

# x,y,z all will have same result 
print("All will Yeild Same Result (x,y,z) respectively :\n")
print("",x,"\n",y,"\n",z)