# Important point to note Python also provide an Array module that provides a compact, typed, and memory-efficient array data structure
# which are closer to c arrays 
# at last they are compared with the python default lists.

'''All Lists methods'''

lst = [1, 2, 3]

# append(x) --> adds an item to end of the lists 
# lst.append(4)
# print(lst)

# extend(iterable) --> adds all item of another iterable
# lst.extend([5, 6])
# print(lst)

# insert(index, x) --> insert the element at given index
# lst.insert(0, 0)
# lst.extend([5, 6])
# print(lst)

# remove(x) --> removes the first matching value
# lst.remove(2)
# print(lst)

# pop() --> remove and return the item at index but by default it act on last item
# x = lst.pop(-2)
# y = lst.pop()
# print(x, y)

# clear() --> remove all elements
# lst.clear()
# print(lst)

# index(x, start=0, end=len) --> return index of first matching value in a range of index but by default the range 0 to length of the list
# x = lst.index(2)
# print(x)

# count(x) --> counts how many time an element appears in the list
# print(lst.count(2))

# sort(key=none, reverse=False) --> sort list in place and a key and order can be changed
# lst.sort()

# reverse() --> reverse the list in place 
# lst.reverse()
# print(lst)

# copy() --> shallow copy of the list
# new_lst = lst.copy()
# print(new_lst)


'''
Core Differnce between lists and array.array

list --> general purpose, dynamic and heterogeous container that stores the references to python objects

Each element is a full Python object with:
  --- type info
  --- reference count
  --- headers
  --- memory allocation
This makes list flexible but heavy.

array.array --> typed memory, memory efficient, homogenous that stores the raw machine values

No Python object per element.
Only machine-level integers/floats.

This makes array:
  -- much smaller memory
  -- faster numeric operations
  -- efficient for binary I/O

'''
