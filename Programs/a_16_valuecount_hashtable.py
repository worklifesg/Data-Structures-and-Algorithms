'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_16 - Value Counting using Hash Tables (in python it is dict)

# using a hashtable to count individual items
# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable object to hold the items and counts
counter = dict()

# TODO: iterate over each item and increment the count for each one
for key in items:
    if (key in counter.keys()):
        counter[key]+=1
    else:
        counter[key]=1

# print the results
print(counter)

'''
Output:
{'apple': 5, 'pear': 3, 'orange': 4, 'banana': 2, 'kiwi': 1}
Time Complexity will grow in linear fashion with increase in items
'''
