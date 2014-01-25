## Searching Algorithms ##



# Sequential Search - Unordered
def sequential(l,item):
    found = False
    i = 0
    while not found and i < len(l):
        if l[i] == item:
            found = True
        else:
            i += 1
    return found



#print sequential([1,3,4,5], 1)

# Sequential Search - Ordered
def ordered_sequential(l, item):
    found = False
    i = 0
    while not found and i < len(l) and l[i] <= item:
        print l[i]
        if l[i] == item:
            found = True
        else:
            i += 1
    return found


#print ordered_sequential([1,3,4, 9,12], 12)



# Binary Search - Iterative
def binary_iterative(l, item):
    found = False
    while not found and len(l) >= 1:
        i = len(l) / 2
        print l[i]
        if l[i] == item:
            found = True
        elif l[i] < item:
            l = l[i+1:]
        else:
            l = l[:i]
    return found


#print binary_iterative([1,2,3,4,5],2)


# Binary Search - Recursive
def binary_recursive(l, item):
    if len(l) == 0:
        return False
    i = len(l) / 2
    if l[i] == item:
        return True
    else:
        if l[i] < item:
            return binary_recursive(l[i+1:], item)
        else:            
            return binary_recursive(l[:i], item)
            
#print binary_recursive([0], 0)









# 


