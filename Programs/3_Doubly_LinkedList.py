'''
Programming Foundations: Algorithms
Data Structures and Algorithm LinkedIn learning course
@ Instructor: Joe Marini: Senior Developer Advocate at Google, Developer

These codes are written while learning algorithms codes during the lecture side-by-side
They might be not exactly same as instructed.
'''

#Program_3 - Doubly Linked List Example


class Node(object):
    # Doubly linked node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, data):
        # Append an item 
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item

        self.count += 1

    def print_foward(self):
        for node in self.iter_forward():
            print(node)
    def print_backward(self):
        for node in self.iter_backward():
            print(node)
            
    def iter_forward(self):
        # Iterate the list
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val
    def iter_backward(self):
        # Iterate the list
        current = self.tail
        while current:
            item_val = current.data
            current = current.prev
            yield item_val
    def insert_start(self, data):        
        if self.head is not None:
            new_node = Node(data, None, None)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.count += 1

    def search_item(self, val):
         for node in self.iter_forward():
            if val == node:
                return True
         return False

items = doubly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')

items.insert_start("Perl")

print("Items in forward direction in the Doubly linked list: ")
print(items.print_foward())
print("Items in backward direction in the Doubly linked list: ")
print(items.print_backward())
print("Number of items of the  Doubly linked list:",items.count)
print("\n")
if items.search_item('SQL'):
    print("True")
else:
    print("False")
