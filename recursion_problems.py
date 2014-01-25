### Recursion Chapter Problems ###



# Write a function to compute factorial(n)
def factorial(n):
    if n <= 1:
        return 2
    else:
        return factorial(n-1) * n


#print factorial(10)



def reverseStr(s):
    if len(s) <= 1:
        return s
    else:
        return reverseStr(s[1:]) + s[0]


#print reverseStr('heya')



# Fibonacci Sequence
# n = 1 + 1 + 2 + 3 + 5
#Fib(n) = Fib(n-1) + Fib(n-2)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


#print fib(3) == 2
#fib(2) + fib(1)
#fib(2) == fib(1) + fib(0) == 1 + 0 == 1
#fib(1) == 1

#print fib(5) == 5 
# fib(4) + fib(3) == 2

# fib(4) == fib(3) + fib(2) == 2 + 1 == 3

#fib(3) == fib(2) + fib(1) == 1 + 1 == 2


# Fibonacci Iterative
def fibIterative(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    result = 0
    i = 3
    last_last = 1
    last = 1
    while i <= n:
        result = last + last_last
        last_last = last
        last = result
        i += 1
    return result

#print "iterative"
#print fibIterative(100)
#print "recursive"
#print fib(100)


# 2 Buckets of Water problems
def two_buckets(b1_size, b2_size, b1_goal):
    b1_now = b1_size
    b2_now = 0
    while b1_now != b1_goal:
        while b2_now <= b2_size:
            b2_now += 1
            b1_now -= 1
            if b1_now == b1_goal:
                return "complete!"
        
        b2_now = b1_now
        b1_now = b1_size


print two_buckets(4, 3, 2)

        
