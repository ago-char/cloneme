# type which are castable are casted using: data_type(castable_value) for example int("2044") makes str:"2044" to int:2044

a="10"
b="20"

# if  you add a to b, you won't get 30 coz addition is done between integers or floating values, if both args of '+' operator are string then it will concatinate them so answer will be: 1020
print(a+b)

# you can use typecasting which will make a="10" to be 10 and b="20" to be 20, now 10 and 20 both are integers they can be added 
print(int(a)+int(b))


a=10
b=20

# well no casting needed here 
print(a+b)

# now int type a is casted to str and so in case of b, now they can not be added but can be concatinated 
print(str(a)+str(b))

# variables should be castabe, casting a="sagar" to int does not provide any of sence, so be aware 
a="sagar"
num=int(a) # throws error