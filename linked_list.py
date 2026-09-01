"""
A linked list is basically a connection of nodes.
Each node contains two things. 
value |  next
for example 
[A | next] ->[B | next] ->[C | None]
so each node says "Here is my value and here is where next node is.
The final node points to None because ther is nothing after it. 

Python list vs linked list ,we can directly access any number in list using list[1]. 
but in linked list it can not be done like this as it have to go through one by one to get the target. 
so basically linked-list indexing/search is generally O(n)
"""
class Node:
    def __init__(self, data ):
        self.data = data
        self.next = None


node1= Node(10)
node2= Node(20)
node3 = Node(30)
# At this point they are completely seprate and not connected.
# Connecting nodes 
node1.next = node2
node2.next = node3

# Now we actually have linked list it 
# The connection are  10->20->30->None
# so how we travese on that 
current = node1
print(current.data)

current = current.next
print(current.data)

current = current.next
print(current.data)

# Do this in a single loop 
current = node1
while current is not None:
    print(current.data)
    current=current.next

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_the_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head  = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def delete_node(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
            

    def display(self):
        current =self.head()
        while current is not None:
            print(current.data)
            current = current.next

my_list  = Linked_list()
my_list.insert_at_begining(10)
print(my_list.head.data)