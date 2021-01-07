'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_9 - Bubble Sort Algorithm

def bubbleSort(dataset):
    
    #loop for examing every element and we will decrement each time from start to the end

    for i in range(len(dataset)-1,0,-1): #stop at 0th item and decrement by -1 each time
        for j in range(i):
            if dataset[j] > dataset[j-1]:
                temp = dataset[j]
                #switch loop
                dataset[j] = dataset[j+1]
                dataset[j+1]=temp

        print('Current state: ',dataset)

def main():
    list1 = [6,20,8,19,56,23,87,41,49,53]
    bubbleSort(list1)
    print('Result: ',list1)


if __name__ == '__main__':
    main()

'''
Output:
Current state:  [6, 8, 19, 56, 20, 87, 23, 49, 41, 53]
Current state:  [6, 19, 8, 20, 87, 56, 23, 41, 49, 53]
Current state:  [6, 8, 20, 19, 56, 23, 41, 87, 49, 53]
Current state:  [6, 20, 8, 56, 19, 41, 23, 87, 49, 53]
Current state:  [6, 8, 56, 20, 19, 41, 23, 87, 49, 53]
Current state:  [6, 56, 8, 19, 20, 41, 23, 87, 49, 53]
Current state:  [6, 8, 19, 56, 20, 41, 23, 87, 49, 53]
Current state:  [6, 19, 8, 56, 20, 41, 23, 87, 49, 53]
Current state:  [6, 19, 8, 56, 20, 41, 23, 87, 49, 53]
Result:  [6, 19, 8, 56, 20, 41, 23, 87, 49, 53]
'''
