'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_13 - Ordered List Search

'''
Sorted search way is much more efficient than unordered list search
With sorted list, we can perform a binary search easily
'''


items = [6,20,8,19,56,23,87,41,49,53]
items.sort()

def binarysearch(items,itemslist):
    listsize = len(itemslist)-1 #size of list
    lowerIdx = 0 #lowest index
    upperIdx = listsize #highest index

    while lowerIdx <= upperIdx:
        pass
        #calculate midpoint
        midpoint = (lowerIdx+upperIdx)//2
        #if item is found return index
        if itemslist[midpoint]==items:
            return midpoint
        #else get the next midpoint
        if items > itemslist[midpoint]:
            lowerIdx = midpoint+1
        else:
            upperIdx = midpoint-1
    if lowerIdx > upperIdx: #if two index has crossed each other it means it is not in the list
        return None

print(binarysearch(23,items))
print(binarysearch(87,items))
print(binarysearch(250,items))

'''
Output:
4
9
None
'''
