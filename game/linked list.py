class Node:
 
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 
# Linked List class contains a Node object
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
 
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
   
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print ("The given previous node must inLinkedList.")
            return
 
        new_node = Node(new_data)
 
        new_node.next = prev_node.next

        prev_node.next = new_node
 
 
    
    def append(self, new_data):
        
        new_node = Node(new_data)
 

        if self.head is None:
            self.head = new_node
            return
 
        last = self.head
        while (last.next):
            last = last.next
 

        last.next =  new_node
 
 

    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
 
 
 
llist = LinkedList()
llist.append(6)
llist.push(7);
llist.push(1);
llist.append(4)
llist.insertAfter(llist.head.next, 8)
print ('Created linked list is:'),
llist.printList()


