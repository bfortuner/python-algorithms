## Sorting Algorithms ##

import random

# Bubble Sort - ascending - My Implementation
def bubble_sort(l):
    sorted = False
    while not sorted:
        sorted = True
        i = 1
        while i < len(l):
            if l[i-1] > l[i]:
                sorted = False
                current = l[i]
                l[i] = l[i-1]
                l[i-1] = current
                i += 1
            else:
                i += 1
    return l



#print bubble_sort([4,1])

# Bubble Sort - Textbook implementation
# Uses two for loops, with one progressing backwards from end of list
# Takes advantage of the fact that at the end of each loop, the next greatest number is in place
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1): # Passnum = 5,4,3,2,1
        for i in range(passnum): # i = 1,2,3,4,5, -- 1,2,3,4 -- 1,2,3 -- 1,2 - 1
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp



# Selection Sort
# Each pass through list it saves the largest value and swaps with the last item
def selection_sort(l):
    i = 0
    while i < len(l):
        largest = l[0]
        largest_pos = 0
        j = 1
        while j < (len(l) - i):
            if l[j] > largest:
                largest_pos = j
                largest = l[j]
                j += 1
            else:
                j += 1
        
        l[largest_pos] = l[j-1]
        l[j-1] = largest
        i += 1
    return l


print selection_sort([3,2,3,4,5,6,2,2,3,4])


# Insertion Sort
# Loops through entire list 1x
# Maintains a sublist on the left side
# For each item in loop, it finds the appropriate position in the sublist
# And then shifts the whole list to the right
def insertion_sort(alist):
    sublist = []
    for i in range(len(alist)):
        placed = False
        for j in range(len(sublist)):
            if alist[i] < sublist[j]:
                placed = True
                sublist = sublist[:j] + [alist[i]] + sublist[j:]
                break
            else:
                pass
        if not placed:
            sublist.append(alist[i])
    return sublist
                
sub = [1,2,3]
l1 = [3,2,1,4,3]

#print insertion_sort(l1)


# Insertion Sort - Textbook - No sublist
# This doesn't maintain a separate sublist
# Each loop, it keeps swapping current value backwards until
# it finds a value that is less than the current value
# Then it stops and goes to the next value
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

# k = 0
# while not end
# Sort 0,3,6 using insertion sort variant w gap
    # keep track of location of next element in sublist
    # Add 3 each time
    # Compare that value one-at-a-time backwards using 3 as increment
    # until it reaches k (which is 0 the first time)
    # Then it skips 3, checks if is position is greater than length of list
    # if position is > length of list, it changes end to True
    # increments k += 1

# After gap items are sorted, so a normal insertion sort
# Complete


# Sub-insertion sort function that takes gap into account





# Shell Sort
def shell_sort(alist, gap=3):
    i = 0
    while i < len(alist)/gap:
        alist = gapInsertionSort(alist, i, gap)
        i += 1
    return gapInsertionSort(alist, 0, 1)


# Gap Insertion Sort (for Shell Sort)
l2 = [9,8,7,6,5,4,3,2,1]
def gapInsertionSort(alist, start_pos, gap):
    for index in range(start_pos+gap, len(alist), gap): # 9, 6, 3, end!
        current_value = alist[index]
        position = index
        while position > start_pos and current_value < alist[position-gap]:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = current_value
    return alist
    


l1 = [54,26,93,17,77,31,44,55,20]
l2 = [9,8,7,6,5,4,3,2,1]
#print gapInsertionSort(l1, 0, 3)
#print shell_sort_2(l1, 3)




# Sort the left side and right side separately, then return right_side + left_side!
# Merge Sort!
def merge_sort(alist):

    if len(alist) <= 1:
        return alist

    else:
        midpoint = len(alist)/2
        lefthalf = alist[:midpoint]
        righthalf = alist[midpoint:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        sorted_list = []
        left_i = 0
        right_i = 0

        while left_i < len(lefthalf) and right_i < len(righthalf):

            if lefthalf[left_i] <= righthalf[right_i]:
                sorted_list += [lefthalf[left_i]]
                left_i += 1

            else:
                sorted_list += [righthalf[right_i]]
                right_i += 1

        if right_i < len(righthalf):
            sorted_list += righthalf[right_i:]
        
        elif left_i < len(lefthalf):
            sorted_list += lefthalf[left_i:]

        return sorted_list




#l1 = [54,26,93,17,77,31,44,55,20]
#print merge_sort(l1)








## Quick Sort ##
def quick_sort(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quick_sort(alist,first,splitpoint-1)
        quick_sort(alist,splitpoint+1,last)
    return alist

# Helper function that sorts sublists
def partition(alist, first, last):
    pivot_value = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while alist[leftmark] <= pivot_value and leftmark <= rightmark:
            leftmark += 1
        while alist[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            tmp = alist[rightmark]
            alist[rightmark] = alist[leftmark]
            alist[leftmark] = tmp

    alist[first] = alist[rightmark]
    alist[rightmark] = pivot_value

    return rightmark


#l1 = [54,26,93,17,77,31,44,55,20]
#l2 = [random.randrange(1,200) for i in range(1,1000)]
#l3 = [31, 26, 20, 17, 44]
#l4 = [26,31]
#print partition(l1, 0, 8)
#print quick_sort(l1)
#print partition(l4)

alist = [54,26,93,17,77,31,44,55,20]

#print quick_sort(alist,0,len(alist)-1)
#print(alist)




#Sorting Algorithm Comparisons

import time, timeit, random

l1 = [54,26,93,17,77,31,44,55,20]
l2 = [random.randrange(1,200) for i in range(1,201)]
print l1




# Bubble Sort
b1 = timeit.Timer("bubble_sort(l1[:])", "from __main__ import bubble_sort, l1")
b2 = timeit.Timer("bubble_sort(l2[:])", "from __main__ import bubble_sort, l2")
#print "Bubble Sort --> Small --> %.9f" % b1.timeit(number=1000)
#print "Bubble Sort --> Large --> %.9f" % b2.timeit(number=1000)

# Selection Sort
s1 = timeit.Timer("selection_sort(l1[:])", "from __main__ import selection_sort, l1")
s2 = timeit.Timer("selection_sort(l2[:])", "from __main__ import selection_sort, l2")
#print "Selection Sort --> Small --> %.9f" % s1.timeit(number=1000)
#print "Selection Sort --> Large --> %.9f" % s2.timeit(number=1000)

# Insertion Sort
i1 = timeit.Timer("insertion_sort(l1[:])", "from __main__ import insertion_sort, l1")
i2 = timeit.Timer("insertion_sort(l2[:])", "from __main__ import insertion_sort, l2")
#print "Insertion Sort --> Small --> %.9f" % i1.timeit(number=1000)
#print "Insertion Sort --> Large --> %.9f" % i2.timeit(number=1000)

# Shell Sort
sh1 = timeit.Timer("shell_sort(l1[:])", "from __main__ import shell_sort, l1")
sh2 = timeit.Timer("shell_sort(l2[:])", "from __main__ import shell_sort, l2")
#print "Shell Sort --> Small --> %.9f" % sh1.timeit(number=1000)
#print "Shell Sort --> Large --> %.9f" % sh2.timeit(number=1000)

# Merge Sort
m1 = timeit.Timer("merge_sort(l1[:])", "from __main__ import merge_sort, l1")
m2 = timeit.Timer("merge_sort(l2[:])", "from __main__ import merge_sort, l2")
#print "Merge Sort --> Small --> %.9f" % m1.timeit(number=1000)
#print "Merge Sort --> Large --> %.9f" % m2.timeit(number=1000)
#print l1
#print l2

# Quick Sort
q1 = timeit.Timer("quick_sort(l1[:], 0, len(l1)-1)", "from __main__ import quick_sort, l1")
q2 = timeit.Timer("quick_sort(l2, 0, len(l2)-1)", "from __main__ import quick_sort, l2")
#print "Quick Sort --> Small --> %.9f" % q1.timeit(number=1000)
print "Quick Sort --> Large --> %.9f" % q2.timeit(number=1000)


'''
for i in range(1000,1000000,20000):
    x = list(range(i))
    t1 = Timer("x[random.randrange(%d)]" % i,"from __main__ import random, x")
    #print t1.timeit(number=1000)
'''
