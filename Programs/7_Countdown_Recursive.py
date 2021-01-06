'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_7 - Countdown counter using recursive technique

def countdown(x):
    if x==0: #breaking condition
        print('Done !')
    else:
        print(x,'....')
        countdown(x-1)

#countdown(10)

'''
Output:
10 ....
9 ....
8 ....
7 ....
6 ....
5 ....
4 ....
3 ....
2 ....
1 ....
Done !
'''

#usage of return statement
def countdown1(x):
    if x==0: #breaking condition
        print('Done !')
        return
    else:
        print(x,'....')
        countdown1(x-1) #function goes back to the starting of the function
        print('ABC')

countdown1(10)

'''
Inference: So with use of return statement and giving print command in else, it prints that statament 'n' times at the end 
as the stack is being unwound after the final return statement

Output:
10 ....
9 ....
8 ....
7 ....
6 ....
5 ....
4 ....
3 ....
2 ....
1 ....
Done !
ABC
ABC
ABC
ABC
ABC
ABC
ABC
ABC
ABC
ABC

'''
