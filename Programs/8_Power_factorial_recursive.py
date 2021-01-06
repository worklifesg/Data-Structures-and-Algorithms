'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_8 - Implement Power and Factorial functions using recursive technique

def power(num,pwr):
    #breaking condition
    if pwr==0:
        return 1
    else:
        return num*power(num,pwr-1)

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))

'''
Output:
5 to the power of 3 is 125
1 to the power of 5 is 1
4! is 24
0! is 1
'''
