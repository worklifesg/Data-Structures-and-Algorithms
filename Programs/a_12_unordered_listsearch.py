'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_12 - Unordered List Search (Linear Search)

'''
After looking at the sorting, we will see how to search within the collections of data
Unordered - currently not sorted in any list
'''

items = [6,20,8,19,56,23,87,41,49,53]

# we don't know yet where the items are there in the list
#so we have to search within the list item by item

def find_item_list(item,itemlist):
    for i in range(0,len(items)):
        #to search for arbitary fields
        if item == itemlist [i]:
            return i
    return None


print(find_item_list(87,items))
print(find_item_list(250,items))

'''
It is inefficient as it has Big O as the function searches item every index by index.
Output:
6
None
'''
