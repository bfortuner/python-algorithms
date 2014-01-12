##### Intro Algorithms In Python Notes ####
import time


### Section 1 - Algorithm Analysis ###

# Sum of first n integers - Naive Approach w iteration
def sum_first_integers_naive(n):
    start = time.time()
    result_sum = 0
    for i in range(n+1):
        result_sum += i
    end = time.time()
    return result_sum, end - start

#Big-O: O(n), Linear

# Use time module to display running time
#for i in range(5):
#    print "Sum is %d required %10.7f seconds" % sum_first_integers_naive(1000000)
#print sum_first_integers(10)


# Sum of first n integers - Formula no iteration
def sum_first_integers_formula(n):
    start = time.time()
    result_sum = (n*(n+1))/2
    end = time.time()
    return result_sum, end-start

# Big-O: O(1), Constant

# Use time module to display running time
#for i in range(5):
#    print "Sum is %d required %10.7f seconds" % sum_first_integers_formula(1000000)



# Minimum num in list - Quadratic
def min_in_list(l):
    if len(l) == 1:
        return l[0]
    min_num = l[0]
    tmp_min = l[0]
    for i in l:
        for j in l:
            if j < i:
                tmp_min = j
        if tmp_min < min_num:
            min_num = tmp_min
    return min_num

# Big-O: O(n^2)
#print min_in_list([0,1])



# Minimum num in list - Linear
def min_in_list_quadratic(l):
    min_num = l[0]
    for i in l[1:]:
        if i < min_num:
            min_num = i
    return min_num

# Big-O: o(n)
#print min_in_list_quadratic([1,3,5])



# Anagram helper functions
def find_pos_in_list(chr, l):
    pos = None
    for i in range(len(l)): # runs from 0 to 3, inclusive (len(list) - 1)
        if l[i] == chr:
            pos = i
            break
    return pos

def gen_list_from_str(s):
    new_list = []
    for e in s:
        new_list.append(e)
    return new_list
    
#print gen_list_from_str('hey there')
#print find_pos_in_list('a',[1,'hi','b','d','e','a','d'])


# Are two strings Anagrams?
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s2_list = gen_list_from_str(s2) # O(n)
    for e in s1: # O(n)
        if e in s2_list:
            chr_pos = find_pos_in_list(e, s2_list) # O(n)
            s2_list[chr_pos] = None
        else:
            return False
    return True

# Big-O: O(n^2)

#print is_anagram('python','typhon')
#print is_anagram('python','typhonnn')


# Convert list to string
def list_to_str(l):
    new_str = ''
    for e in l:
        new_str += e
    return new_str


# Help Sorting Function for Anagrams - Selection Sort or Insertion Sort?
def sort_str(s):
    new_list = gen_list_from_str(s)
    for i in range(len(new_list)):
        for j in range(i+1, len(new_list)):
            if new_list[j] < new_list[i]:
                tmp_j = new_list[j]
                new_list[j] = new_list[i]
                new_list[i] = tmp_j
    return list_to_str(new_list)


# Anagram Comparison w Sorting
def is_anagram_sorting(str1, str2):
    new_str1 = sort_str(str1)
    new_str2 = sort_str(str2)
    return new_str1 == new_str2

#print is_anagram_sorting('python','typhon')

# Big-O: O(n^2)




# Anagram Count + Sort
def count_same_letters(str1, str2):
    l1 = [0]*26
    l2 = [0]*26
    for e in str1:
        l1[ord(e) - ord('a')] += 1
    for e in str2:
        l2[ord(e) - ord('a')] += 1
    return l1 == l2

#print count_same_letters('python', 'typhon')

# Big-O: O(n), but sacrificed memory space to store the 2 lists!



# Analyzing Python List Operations
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


# Python timit module
from timeit import *

t1 = Timer("test1()", "from __main__ import test1")
#print ("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
#print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
#print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
#print("list range ",t4.timeit(number=1000), "milliseconds")


# Comparison of pop() vs pop(i)
l1 = list(range(2000000))
def pop1():
    l1.pop()
    return l1

def pop2():
    l1.pop(0)
    return l1

# Timeit module test functions for pop()
t1 = Timer("pop1()", "from __main__ import pop1")
#print t1.timeit(number=1000)
t2 = Timer("pop2()", "from __main__ import pop2")
#print t2.timeit(number=1000)




# Test list index operator runtime
"""
for i in range(1000,1000000,20000):
    x = list(range(i))
    t = Timer("x[random.randrange(%d)]" % i,"from __main__ import random, x")
    print i, t.timeit(number=1000)
"""

import random

def test_list_del(l, num):
    rand_index = random.randrange(num)
    #del x[rand_index]


def test_dict_del(l, num):
    rand_index = random.randrange(num)
    #del x[rand_index]


# Compare del with list vs dict
"""
for i in range(1000,1000000,20000):
    x_list = list(range(i))
    list_t = Timer("test_list_del(%s, %d)" % (x_list, i),"from __main__ import random, x_list, test_list_del")
    list_time = list_t.timeit(number=1000)
    x_dict = {j:None for j in range(i)}
    dict_t = Timer("test_dict_del(%s, %d)" % (x_dict, i),"from __main__ import random, x_dict, test_dict_del")
    dict_time = dict_t.timeit(number=1000)
    print "i: %d, list: %.9f, dict: %.9f" % (i, list_time, dict_time)
"""



# Find the kth smallest number in unsorted list of nums
#num_list = list(range(10))
#random.shuffle(num_list)

def sort_list(new_list):
    for i in range(len(new_list)):
        for j in range(i+1, len(new_list)):
            if new_list[j] < new_list[i]:
                tmp_j = new_list[j]
                new_list[j] = new_list[i]
                new_list[i] = tmp_j
    return new_list

def find_kth_smallest_num(l, k):
    sortedlist = sort_list(l)
    return sortedlist[k-1]

#print find_kth_smallest_num(num_list, 6)




