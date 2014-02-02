## Sorting Problems ##




# Random List of Ints

l1 = [2,5,3,7,4]

#Bubble
#while False
[2,5,3,7,4]
[2,3,5,7,4]
[2,3,5,4,7]
[2,3,4,5,7]
#True - Done!

l1 = [2,5,3,7,4]
#Selection
[2,5,3,7,4]
[2,3,5,7,4]
[2,3,4,7,5]
[2,3,4,5,7]

l1 = [2,5,3,7,4]
#Insertion
[2,5,3,7,4] # saved_value = 5, compares to 2, stops
[2,5,3,7,4] # saved_value = 3, compares to 5, shifts 5 up, compares to 2, stops
[2,3,5,7,4] # saved_value = 7, compares to 5, stops
[2,3,5,7,4] # saved_value = 4, compares to 7, shifts 7 up, compares to 5, shifts 5, stops
[2,3,4,5,7]

#Insertion Sort Implementation
def bad_insertion_sort(alist):
    start = 0
    while start < len(alist)-1:
        start += 1
        current_value = alist[start]

        tmp = start - 1
        while tmp >= 0:

            if alist[tmp] > current_value:
                alist[tmp+1] = alist[tmp]
                tmp -= 1

            else:
                alist[tmp+1] = current_value
                break
    return alist

#print insertion_sort(l1)


# Textbook Insertion Sort
def insertion_sort(alist, gap, start):
    for index in range(start+gap, len(alist), gap):
        compare_value = alist[index]
        position = index 

        while position>0 and compare_value < alist[position-gap]:
            alist[position] = alist[position-gap]
            position -= gap

        alist[position] = compare_value

    return alist

#print insertion_sort(l1,2,0)




l1 = [2,5,3,7,4]
#Shell Sort
# Gap = 2
[2,5,3,7,4] # Select 2nd element in gap interval == 3
[2,5,3,7,4] # Compare 3 to first gap element, 2, stops
[2,5,3,7,4] # Grab second gap interval 4, compare to 3, stop
[2,5,3,7,4] # Increment starting element, 5, compare to 7, stop
[2,5,3,7,4] # Increment starting element, 3, compare to 4, stop
# Now do a standard insertion sort w gap 1
[2,3,4,5,7]


l1 = [2,5,3,7,4]
l2 = [7,20,3,13,5,4,12,2,6]

# Shell Sort Implementation
def shell_sort(alist,gap):
    i = 0
    while i < len(alist) / gap:
        alist = gap_insertion_sort(alist, i, gap)
        i += 1
    return gap_insertion_sort(alist,0,1)

# Helper Insertion Sort
def gap_insertion_sort(alist, start, gap):
    for index in range(start+gap, len(alist), gap):
        compare_value = alist[index]
        position = index 

        while position>start and compare_value < alist[position-gap]:
            alist[position] = alist[position-gap]
            position -= gap

        alist[position] = compare_value

    return alist


#print gap_insertion_sort(l2,3,0)
#print shell_sort(l1,2)
#print "starting shell sort ------"
#print shell_sort(l2,2)
#print "ending shell sort ------"


l1 = [2,5,3,7,4,8]
#Merge
#[5,2,7,3] 
#[5,2] -- [7,3] #Recursively split list/2
#[5] - [2] - [7] - [3] #Reach base case, return single element
#[2,5] -- [3,7] #Sort and merge sublists of size 1
#[2,3,5,7] #Sort and merge sublists of size 2

# Merge Sort Implementation
def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    else:
        midpoint = len(alist)/2
        left = merge_sort(alist[:midpoint])
        right = merge_sort(alist[midpoint:])

        newlist = []

        while len(left)>0 and len(right)>0:
            if left[0] < right[0]:
                newlist.append(left[0])
                left = left[1:]
            else:
                newlist.append(right[0])
                right = right[1:]

        if len(left) > 0:
            newlist += left
        else:
            newlist += right

    return newlist


l1 = [2,5,3,7,4]
#print merge_sort(l1)



l1 = [2,5,3,7,4]
#Quick Sort




def quick_sort_helper(alist,first,last):
    # sort the list
    pivot = alist[first]
    left = first + 1
    right = last

    while right >= left:

        while left <= right and alist[left] < pivot:
            left += 1

        while right >= left and alist[right] > pivot:
            right -= 1

        if right > left:
            tmp = alist[left]
            alist[left] = alist[right]
            alist[right] = tmp
            right -= 1
            left += 1
        else:
            break

    alist[0] = alist[right]
    alist[right] = pivot
    return right


# Quick Sort Implementation
def quick_sort(alist, first, last):
    print alist[first:last+1]
    if first < last:
        splitpoint = quick_sort_helper(alist,first,last)
        quick_sort(alist,first,splitpoint-1)
        quick_sort(alist,splitpoint+1,last)
    return alist


l3 = [6,3,2,8,1]
l4 = [1,3,2]
l5 = [3,2]
#[1, 3, 2, 6, 8]
#print quick_sort_helper(l4,0,2)
#print quick_sort_helper(l5,0,1)
print quick_sort(l3,0,len(l3)-1)
#print l3
#print quick_sort(l3,0,2)
#print quick_sort_helper(l4,0,2)
#print l3
#print quick_sort(l3,1,2)















