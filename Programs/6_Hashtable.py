'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_6 - Hash Table Example

# Create a hashtable all at once using dict() constructor

items1 = dict({'key1':1,'key2':2,'key3':'three'})
print(items1)

#Creata a hashtable progessively as these tables can grow and shrink to fit the data they contain

items2 = {} #empty dict
items2['key1'] = 1
items2['key2'] = 2
items2['key3'] = 'three'
print(items2)

#Try to access non-existant key
'''
print(items1['key6'])

--- Error comes
KeyError: 'key6'
---- because that key is not added to items1
'''

# Replace an item

items2['key2']='two'
print(items2)

#Iterate all keys and values in dictionary

for key, value in items2.items():
    print('Key: ',key,'Value: ',value)

'''
Output:
{'key1': 1, 'key2': 2, 'key3': 'three'}
{'key1': 1, 'key2': 2, 'key3': 'three'}
{'key1': 1, 'key2': 'two', 'key3': 'three'}
Key:  key1 Value:  1
Key:  key2 Value:  two
Key:  key3 Value:  three
'''
