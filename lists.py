##### Lists #####



# Implement Python List w Linked List
class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.last = None

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
        self.length = 0

    def __str__(self):
        result = '['
        current_node = self.head
        while current_node != None:
            result = result + str(current_node.getItem()) + ', '
            current_node = current_node.getNext()
        return result + ']'

    def isEmpty(self):
        return self.head == None

    def add(self, value):
        new_node = Node(value)
        new_node.setNext(self.head)
        self.head = new_node
        self.length += 1

    def size(self):
        current_node = self.head
        node_count = 0
        while current_node != None:
            node_count += 1
            current_node = current_node.getNext()
        return node_count

    def size2(self):
        return self.length

    def search(self, value):
        current_node = self.head
        found = False
        while current_node != None and not found:
            if current_node.getItem() == value:
                return True
            else:
                current_node = current_node.getNext()
        return found

    def remove(self, value):
        if self.size() == 0:
            return
        if self.head.getItem() == value:
            self.head = self.head.getNext()
            self.length -= 1
            return
        prior_node = self.head
        while prior_node.getNext() != None:
            current_node = prior_node.getNext()
            if current_node.getItem() == value:
                prior_node.setNext(current_node.getNext())
                self.length -= 1
                return
            else:
                prior_node = current_node
                current_node = current_node.getNext()
        return


    # Append new node to end of list - O(n)
    def append(self, value):
        new_node = Node(value)
        current = self.head
        if current == None:
            self.head = new_node
            return
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(new_node)
        self.length += 1

    # Append new node to end of list - O(1)
    def append_constant_time(self, value):
        new_node = Node(value)
        self.last.setNext(new_node)
        self.last = new_node
        
    # Add new item at position pos in list - O(n)
    def insert(self, pos, value):
        self.length += 1
        if pos == 0:
            self.add(value)
            return
        new_node = Node(value)
        count = 0
        current = self.head
        prior = None
        while count < pos and current != None:
            prior = current
            current = current.getNext()
            count += 1
        new_node.setNext(current)
        prior.setNext(new_node)
        
    # Return position of value in list - O(n)
    def index(self, value):
        pos = 0
        current = self.head
        while current != None and current.getItem() != value:
            current = current.getNext()
            pos += 1
        if current == None:
            return None
        else:
            return pos

    # Remove element in position pos or remove last element
    def pop(self, pos=None):
        if self.size() == 0:
            return
        if pos == None:
            pos = self.size() - 1
        if pos == 0:
            tmp = self.head.getItem()
            self.head = self.head.getNext()
            return tmp
        current = self.head
        prior = None
        count = 0
        while count < pos:
            prior = current
            current = current.getNext()
            count += 1
        prior.setNext(current.getNext())
        return current.getItem()

    def slice(self, start, stop):
        result = '['
        current_node = self.head
        i = 0
        while i < start:
            current_node = current_node.getNext()
            i += 1
        while i < stop:
            result = result + str(current_node.getItem()) + ', '
            current_node = current_node.getNext()
            i += 1
        return result + ']'


# Test cases for linked list 
ll = LinkedList()
print ll


"""
ll.add('hey')

ll.remove('hey')


ll.add(True)
ll.add('hey')
ll.add('bab')
ll.add(123)
print 'printing __str__'
print ll
print ll.size()
print ll.slice(2,4)
'''
print ll.size2()
print ll.head.getItem()
ll.remove('hey')
print ll.size2()
print ll.head.getItem()
ll.remove('hey')
ll.remove(True)
ll.search('hey')
ll.search(123)
print ll.size2()
print 'removing bogus'
print ll.remove('bogus')

ll.append('brendan')
print ll.search('brendan')
ll.append('colin')
print "------- pop -------"
print ll.pop(0)
print ll.index('colin')
"""



# Ordered List Class
class OrderedList(object):
    def __init__(self):
        self.head = None

    def search(self, value):
        current = self.head
        while current != None and current.getItem() <= value:
            if current.getItem() == value:
                return True
            else:
                current = current.getNext()
        return False

    def add(self, value):
        new_node = Node(value)
        current = self.head
        prior = None
        while current != None and current.getItem() < value:
            prior = current
            current = current.getNext()
        if prior == None:
            self.head = new_node
        else:
            prior.setNext(new_node)
            new_node.setNext(current)


