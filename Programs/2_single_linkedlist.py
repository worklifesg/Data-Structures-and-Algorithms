'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_2 - Linked List Example

#Node class - implement node type that will be stored in the linkedlist (single data field)

class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None #single next means it is single linked list (one direction)

    #getting and setting data field
    def get_data(self):
        return self.val
    def set_data(self,val):
        self.val = val

    #getting and setting next field data
    def get_next(self):
        return self.next
    def set_next(self,next):
        self.next = next    

# Linked List Class

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head #field for the head
        self.count = 0 #intial nodes in the list count

    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO: insert a new node
        new_node = Node(data)
        new_node.set_next(self.head) #current head 
        self.head=new_node#tell head to point to node
        self.count+=1#update the node count

    def find(self, val):
        # TODO: find the first item with a given value
        item = self.head
        while(item!=None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()

        return None

    def deleteAt(self, idx):
        # TODO: delete an item at given index
        if idx > self.count-1:
            return
        #checking if deletion is a head node
        if idx == 0:
            self.head = self.head.get_next()
        else: #we want to advance to the node just one before the one we want to delete
            tempIdx = 0
            node = self.head
            while tempIdx < idx - 1:
                node = node.get_next()
                tempIdx +=1
            node.set_next(node.get_next().get_next()) #once we get the previous node, we point it to next by next node where want to point it to.
            self.count -=1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()
'''
# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13))
print("Finding item: ", itemlist.find(78))
'''
'''
#result Node:  15
Node:  13
Node:  49
Node:  38
Item count:  4
Finding item:  <__main__.Node object at 0x000001E13E126190>
Finding item:  None
'''

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list() 
