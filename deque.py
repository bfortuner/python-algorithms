#### Deques - Hybrid of Queue and Stack ####


# Deque Class Implementation
class Deque(object):
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []

    # Add item to left side of list
    def addFront(self, item):
        self.items.append(item)

    # Add item to RIGHT side of list
    def addRear(self, item):
        self.items = self.items.insert(0,item)

    # Remove and return item on the RIGHT side of list
    def removeFront(self):
        return self.items.pop()

    # Remove and return item on the LEFT side of list
    def removeRear(self):
        return self.items.pop(0)



## Time-complexity ##

# Adding and Removing from FRONT: O(1)
# -- append(item) and pop() methods are O(1)

# Adding and Removing from REAR: O(n)
# -- insert(1,item) and pop(0) methods are O(n)


def isPalindrome(str1):
    deque = Deque()
    for c in str1:
        if c != ' ':
            deque.addFront(c)
    while deque.size() > 1:
        if deque.removeFront() != deque.removeRear():
            return False
    return True


#print isPalindrome(' a b a b')
        
