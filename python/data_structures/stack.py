# start with the operation in stack:
"""
push
view
pop
delete Nth item
"""

stack = [9, 123, 4, 3, 55, 2]
# just like viewing the stack
print(stack)
# pushing the item in the stack
stack.append(99)
print(stack)
# poping out the item
print(stack.pop())
print(stack)
# delete at Nth pos
stack.pop(1)
print(stack)
