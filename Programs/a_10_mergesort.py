'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_10 - Merge Sort Algorithm

items = [6,20,8,19,56,23,87,41,49,53]

def mergesort(dataset):
    #defining segment of breaking array
    if len(dataset)>1: #breaking condition
        mid = len(dataset)//2
        leftarray = dataset[:mid]
        rightarray = dataset[mid:]

        #recursively breaking arrays

        mergesort(leftarray)
        mergesort(rightarray)

        #performing merging
        i=0 #index into left array
        j=0 #index into right array
        k=0 #index into merged array

        #both arrays have content (merging)

        while i < len(leftarray) and j <len(rightarray):
            if leftarray[i] <rightarray[j]:
                dataset[k] = leftarray[i]
                i+=1 #advance left array 
            else:
                dataset[k]=rightarray[j]
                j+=1 #advance tight array
            k+=1 #advanced merge array

        #if arrays have values add it to them

        while i < len(leftarray):
            dataset[k] = leftarray[i]
            i+=1
            k+=1
        while j < len(rightarray):
            dataset[k] = rightarray[j]
            j+=1
            k+=1       

print(items)
mergesort(items)
print(items)

'''
Output:
[6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
[6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
'''
