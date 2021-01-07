'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_14 - Determine Whether the List is Sorted or Not

'''
For large dataset, we need to write algorithm to determine whether the list is sorted or not.
But checking item by item has a big issue of linear time complexity
'''

items1 = [6,8,19,20,23,41,49,53,56,87]
items2 = [6,20,8,19,56,23,87,41,49,53]

def sort(itemlist):
    for i in range(0,len(itemlist)-1):
        #each items is <= the one that comes after
        if (itemlist[i]>itemlist[i+1]):
            return False

    return True

def sort_simple(itemlist):
 
    return all(itemlist[i]<=itemlist[i+1] for i in range(0,len(itemlist)-1))


print(sort(items1))
print(sort(items2))
print('--------------')
print(sort_simple(items1))
print(sort_simple(items2))

'''
True
False
--------------
True
False
'''
