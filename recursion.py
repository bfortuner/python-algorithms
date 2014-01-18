#### Recursion ####



# Iterative sum
def iterativeSum(l):
    total = 0
    for e in l:
        total += e
    return total


# Recursive sum
def recursiveSum(l):
    if len(l) == 1:
        return l[0]
    return l[0] + recursiveSum(l[1:])

 


#l1 = [1,2,3,4,5]
#print iterativeSum(l1)
#print recursiveSum(l1)


# Recursive Factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)



# Recursive Int to Str of any Base
def intToStr(base, n):
    basestr = '0123456789ABCDEF'
    if n < base:
        return basestr[n]
    else:
        return intToStr(base, n/base) + basestr[n % base]


#print intToStr(2, 1453)
 

# Recursive reverse a string
def reverseStr(s):
    if len(s) == 1:
        return s[0]
    else:
        return reverseStr(s[1:]) + s[0]



def isPalindrome(s):
    return s == reverseStr(s)


# Reverse String Using Stack Frame
from stacks import Stack

def stackRevStr(s, stack):
    if len(s) == 0:
        return ''
    elif len(s) == 1:
        result = s
        while not stack.isEmpty():
            result += stack.pop()
        return result
    else:
        stack.push(s[0])
        return stackRevStr(s[1:], stack)

#s1 = Stack()
#print stackRevStr('h',s1)
