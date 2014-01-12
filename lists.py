##### Lists #####



# Implement Python List w Linked List
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

    def setNext(self, new_next):
        self.next = new_next

    def setItem(self, new_item):
        self.item = new_item

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next



class LinkedList(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, value):
        new_node = Node(value)
        new_node.setNext(self.head)
        self.head = new_node

    def size(self):
        current_node = self.head
        if current_node != None:
            node_count = 1
        else:
            node_count = 0
            
        while current_node.getNext() != None:
            node_count += 1
            current_node = current_node.getNext()
        return node_count



ll = LinkedList()
#print ll.isEmpty()
#print ll.head
n1 = Node('hey')
#print ll.head
n2 = Node(4)
n3 = Node(True)

#print n1.getItem()
#print n2.getItem()
#print n3.getItem()

ll.add(n1)
ll.add(n2)
ll.add(n2)

head = ll.head
head.getItem()

#print ll.size()    
#print ll.isEmpty()
