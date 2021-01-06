'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_4 - Stacks Example

#Create a new empty stack

stack=[]

#Push items onto stack @append function - 4 items on the stack

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

#Print stack contents

print(stack)

#Pop an item off the stack - give us a value back

x = stack.pop()
print(x)
print(stack)

'''
Output:
[1, 2, 3, 4]
4
[1, 2, 3]
'''
