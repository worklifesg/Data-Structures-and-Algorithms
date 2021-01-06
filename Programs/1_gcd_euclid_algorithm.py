'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_1 - Euclid's Algorithm - To find greatest common denominator (GCD) of 2 integers

def euclid(a,b):
    #writing a while loop where stopping the code if b=0

    while (b != 0):
        t=a #temporary variable t
        a=b

        b=t%b # here t%b means remainder r = a/b
    
    return a

print(euclid(60,96)) #should be 12
print(euclid(20,8)) #should be 4
 
