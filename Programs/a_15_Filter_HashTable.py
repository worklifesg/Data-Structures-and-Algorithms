'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_15 - Filtering using Hash Tables (in python it is dict)
'''
Hash Table are data structures that associates keys with values and values can have different forms.
(numbers, strings, objects)
Keys to the hash tables have to be unique, it give us easy way to implement certian kinds of algorithms
Ex. Reduce list of items by eliminating the duplicates
'''

# use a hashtable to filter out duplicate items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable to perform a filter

filter = dict()

# TODO: loop over each item and add to the hashtable

for key in items:
    filter[key]=0 #remove duplicate items

# TODO: create a set from the resulting keys in the hashtable

result=set(filter.keys())
print(result)

'''
{'kiwi', 'apple', 'banana', 'pear', 'orange'}
Time Complexity will grow in linear fashion with increase in items
'''
