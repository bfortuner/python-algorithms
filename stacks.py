##### Stacks #####


# Implement a Stack class using List

class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def matches(self, s1):
        return s1 == s.peek()

# Check for balanced parentheses in code
def balanced_paren(paren_sequence):
    if len(paren_sequence) % 2 != 0:
        return False
    s = Stack()
    balanced = True
    while s.size() > 0 and balanced:
        if e in ["(","{","["]:
            s.push(e)
        elif e in [")","}","]"]:
            try:
                s1 = s.pop()
                if not s.matches(s1):
                    balanced = False
            except:
                balanced = False

    return balanced and s.isEmpty()

p = "{(([][]))}"
#print balanced_paren(p)


# Stack class test cases
"""
s = Stack()
print s.isEmpty()
s.push(5)
print s.size()
print s.peek()
print s.pop()
print s.isEmpty() 
"""



# Reverse characters in string using stack class
def revstring(mystr):
    s = Stack()
    new_str = ''
    for e in mystr:
        s.push(e)
    while not s.isEmpty():
        new_str += s.pop()
    return new_str

#print revstring('abc')



# Integer (base 10) to other base number (base n)
def base_converter(num, base):
    digits = "0123456789ABCDEFGHIJKLMNOP"
    binary_stack = Stack()
    while num > 0:
        binary_stack.push(num % base)
        num = num / base
    binary_str = ''
    while not binary_stack.isEmpty():
        binary_str += digits[binary_stack.pop()]
    return binary_str

#print base_converter(2453298738763, 26)
print base_converter(17,2)
print base_converter(45,2)
print base_converter(96,2)



# Convert from infix to postfix
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    # ["A","*","B","+","C","*","D"]

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)
        
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

#print(infixToPostfix("A * B + C * D"))
#print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

print infixToPostfix("( A + B ) * ( C + D ) * ( E + F )")
print infixToPostfix("A + ( ( B + C ) * ( D + E ) )")
print infixToPostfix("A * B * C * D + E + F")



def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

#print(infixToPostfix("A * B + C * D"))
#print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


#tl ["A","*","B","+","C","*","D"]

#1 p1 ["A"] 
#1 sl []

#2 p1 ["A"] 
#2 sl ["*"]

#3 p1 ["A","B"] 
#3 sl ["*"]

#4 p1 ["A","B","*"] 
#4 sl ["+"]

#5 p1 ["A","B","*","C"] 
#5 sl ["+"]

#6 p1 ["A","B","*","C"] 
#6 sl ["+","*"]

#7 p1 ["A","B","*","C","D"], #8-9 p1 ["A","B","*","C","D","*","+"]  
#7 sl ["+","*"]





