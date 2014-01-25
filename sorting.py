## Sorting Algorithms ##



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


#print selection_sort([3,2,3,4,5,6,2,2,3,4])


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

print insertion_sort(l1)


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

