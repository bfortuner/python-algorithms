## Hash Tables ##



# Hash Function - Convert str to int
def convert_str_to_int(str):
    sum = 0
    for e in str:
        sum += ord(e)
    return sum

# Hash Function - Add element to Hash Table
def add_value_to_hash_table(buckets, int_key, value):
    bucket = int_key % len(buckets)
    if buckets[bucket] == None:
        buckets[bucket] = [value]
    else:
        buckets[bucket].append(value)
    return buckets

# Basic hash table to store values in n buckets
def build_hash_table(n, values, hash_func='normal'):
    buckets = [None] * n
    for e in values:
        if hash_func == "linear":
            buckets = add_hash_linear_probing(e, buckets)
        else:
            int_key = convert_str_to_int(e)
            buckets = add_value_to_hash_table(buckets, int_key, e)
    return buckets

# Hash Table Lookup
def hash_table_lookup(value, hash_table):
    key = convert_str_to_int(value) % len(hash_table)
    bucket = hash_table[key]
    for e in bucket:
        if e == value:
            return True
    return False



# Hash Function - Linear probing
def add_hash_linear_probing(item, hash_table):
    if type(item) != int:
        int_key = convert_str_to_int(item)
    else:
        int_key = item
    bucket = int_key % len(hash_table)
    if hash_table[bucket] == None:
        hash_table[bucket] = item
        return hash_table
    else:
        placed = False
        while not placed:
            bucket += 1
            if bucket == len(hash_table):
                bucket = 0
            if hash_table[bucket] == None:
                hash_table[bucket] = item
                placed = True
        return hash_table
        

#h1 = build_hash_table(11, ['hey','brendan','colin','david','dad','mom','stephen','kim','mathisen','nenke','matejak'], 'linear')

h2 = build_hash_table(11, [113,117,97,11,114,108,116,105,99],'linear')
#print h2
#for e in h2:
#    print e,






# Hash Function - Convert str to int - WEIGHTED!
def weight_convert_str_to_int(str):
    sum = 0
    i = 1
    for e in str:
        sum += ord(e) * i
        i += 1
    return sum



print weight_convert_str_to_int("abba")
print weight_convert_str_to_int("bbaa")
