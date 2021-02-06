class Node:
    def __init__(self, data):
        self.item = data
        self.next = None  # reference to the next node
        self.pre = None  # reference to the previous node

class DoublyLinkedList:
    def __init__(self):  # when a new instance of the DLL is created, there is nothing in it
        self.head = None
        self.tail = None
    
    
    
    #def sortOrder(self)

    
    def itemSearch(self, value): #search list by name
        x = False
        n = self.head
        head = n
        tail = n  
        while tail.next is not None:  
            tail = tail.next
        while head is not tail:
            if head.item.name == value or tail.item.name == value:
                x = True
                break
            else:
                head = head.next
                tail = tail.pre
        if x:
            if head.item.name == value:
                return head.item
            else:
                return tail.item
        else:
            return None

    def insertToList(self, data): #method add to link list
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.pre = n
    
    def sortNodes(self): #sort list
        if self.head is None:
            return;
        else:
            current = self.head
            while current.next is not None:
                index = current.next
                while index is not None:
                    if (current.item > index.item):
                        temp = current.item
                        current.item = index.item
                        index.item = temp
                    index = index.next
                current = current.next
    
    def traverse(self):
        if self.head is None:
            print("List has no entry")
        else:
            n = self.head
            while n is not None:
                print(n.item, " ")
                n = n.next
    def display(self):    
        #Node current will point to head    
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        print("Nodes of doubly linked list: ");    
        while(current != None):     
            #Prints each node by incrementing pointer.    
            print(current.item.print),;    
            current = current.next;    