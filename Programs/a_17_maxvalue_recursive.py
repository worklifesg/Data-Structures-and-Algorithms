'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_17 - Find Max Value Recursively

# declare a list of values to operate on
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_max(items):
    # TODO: breaking condition: last item in list? return it
    if len(items)==1: 
        return items[0]

    # TODO: otherwise get the first item and call function
    # again to operate on the rest of the list

    op1 = items[0]
    print(op1)
    op2 = find_max(items[1:])
    print(op2)

    # TODO: perform the comparison when we're down to just two
    if op1 > op2:
        return op1
    else:
        return op2


# test the function
print(find_max(items))

'''
Time complexity same as Unordered search list
Output:
87
--------
6
20
8
19
56
23
87
41
49
53
53
53
87
87
87
87
87
87
87
'''
