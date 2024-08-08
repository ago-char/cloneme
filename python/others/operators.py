"""
Operator	Description
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
"""

# I will not talk more on this but just wanna demonstrate difference between is vs ==
l = ["item1", "item2"]
m = ["item1", "item2"]
t = ("t1", "t2")
tuple1 = tuple(l)

# l and m has same value and both are list
print(l == m)  # returns True as they are equal
print(l is m)  # returns False as they are not same obj or referring to same obj
print(
    tuple1 == l
)  # returns False, even if 'tuple1' is tuple version of 'l', it is of different data type
print(
    tuple1 is l
)  # returns False coz they are 2 different objs, it can easily be clear as they are of different data type

print("................\n")
# demonstrating biggest confusion
list1 = l  # same objects
list2 = list(l)  # typecasted version, so not same objs
print(list1 is l)  # returns True as they are same obj
print(list2 is l)  # returns False as they are not same object
