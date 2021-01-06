'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_5 - Queue Example

'''
You can regular list as queue in python but is is inefficient to do so:
removing an item from beginning of the list requires bigger O(n) - Linear Time Complexity
because all the subsequent items have to be shifted down in their slots

In python we have more efficient data structure called Deque (collections module)
'''

from collections import deque

#Create an empty deque object that will function as queue

queue = deque()

#Add some items to queue

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

#print queue contents

print(queue)

#pop an item off the 

x = queue.popleft() #front of the queue
print(x)
print(queue)

'''
Output:
deque([1, 2, 3, 4])
1
deque([2, 3, 4])
'''
