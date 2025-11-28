'''
Magic or dunder or doubleunderscore methods make the objects behave like python built types.
Why magic methods matters ?
Because they let us make custom classes behave like lists, dicts,number, functions, iterators, context manager

'''


''' Tier 1 '''


class Person:
  def __init__(self, name , age):
    self.name = name
    self.age = age 

  def __repr__(self): # returns the string for developers and also machine readable.
    return f'Person({self.name!r}, {self.age!r})'
  
  def __str__(self): 
    return f"{self.name} is {self.age} years old"
  
  def __bool__(self):
    if self.age > 18 and self.age < 64:
      return True
    else:
      return False
    
  def __eq__(self, other):
    if not isinstance(other, Person):
      return NotImplemented
    return (self.name, self.age) == (other.name, other.age)
  
  def __lt__(self, other):
    if not isinstance(other, Person):
      return NotImplemented
    return self.age < other.age
  

p = Person("Alice", 25)
# print(p.name, p.age)

# __init__ () --> object initializer, called right after the object is created, it initilise the instance attributes
# here __new__ creates the empty shell
# __init__ fills it


# __repr__() --> returns the string representation that can be executed to get the same value as the object.
# if we do not define the it ourself, then the out[ut will be the memory address
# when the insatnce of a class is passed to repr() , python will call the repr fucntion automatically.

# important --> When a class doesn’t implement the __str__ method and you pass an instance of that class to the str(), Python returns the result of the __repr__ method.
# because internally the __str__ method calls the __repr__ method.
# print(repr(p))

# __str__() --> returns the descriptive , readable version of the object.
# it fall back to repr func when not defined.
# called by str(obj), print(obj), f"{obj}"
# down below the str method is called automtaically.
# print(p)


# __bool__() --> if an nstance of a class if passed to bool() fucntion it will always return True,
# and if we want to it to give True or False based on some condition then we will implement __bool__ method in the class
# and it will give true or false based on attributes of that instance.
# print(bool(p))

# if their is no __bool__ method in the class then it will look at the __len__ method,
# and if the len is zero, the object is False otherwise it is True.

# __len__() --> used on an iterable object or anything that has length as an attribute, called by len(obj)
# should return a non-negative integer.
# used by built-in code and frameworks to check "how big is this?"


# important --> all obj of custom class return True by default,
# implementing a bool method override default.

class playlist:
  def __init__(self, songs):
    self._songs = list(songs)

  def __len__(self): # here it will shows 1 less in length, just to show how it works no lgical explanantion.
    return len(self._songs) - 1 
  
  def __getitem__(self, index):
    return self._songs[index]
  
  def __setitem__(self,index, value):
    self._songs[index] = value
  
old_songs = playlist(["s1", "s2", "s3", "s4", "s5"])
# print(len(old_songs)) 
old_songs[2] = "a5"
# print(old_songs[2])



# __getitem__() --> indexing/accessing
# make object behaves like lists or dicts,
# and can be called like we we access the elements from a list or dictionary
# implemented in above example and called below

# print(old_songs[0])

# above is for list and down is for dictionary

class Settings:
  def __init__(self):
    self._data = {}

  def __getitem__(self, key):
    return self._data[key]
  
  def __setitem__(self, key, value):
    self._data[key] = value
  
s = Settings()
# ["theme"] = "dark"
# print(s["theme"])


# important --> indexerror should be raised for bad indices 
# and keyerror should be raised missing keys.

# __setitem__() --> assignment of a value at an index or at a key
# implemented in above examples

# Design note: --> getitem + setitem together makes objects feel like conatiner.
# so they should be used together



# __iter__ and __next__ -->
# they are the partners works together and make the object iterable.
# an object must implement these methods to be an iterable.

# __iter__ --> gets the iterator
# __next__ --> produces the value one by one.

# what internally happens: 
# an oter object is created,
# while True loop will run and next method takes each element one by one,
# and does operaton on them,
# finally loops ends with break statement.

# only __iter__ --> just want to loop over the internal data
#use both when object is iteslf iterator


class Counter:
  def __init__(self, limit):
    self.limit = limit
    self.current = 0
  

  def __iter__(self):
    self.current = 0
    return self
  
  def __next__(self):
    '''gives next value  and set current for next value and when limits are crossed it stops'''
    if self.current >= self.limit:
      raise StopIteration
    value = self.current
    self.current += 1
    return value
  
c = Counter(15)
# print(next(c)) 

# important note:
# iteration is stateful as once exhausted iteration is stopped


# __eq__ (==)--> check for equality between the object value of a class.
# NotImplemented matters here when different classes objects are compared
# always return True or False

# implemented in top most class Person
# p alteady craeted
p1 = Person("Alice", 25)
p2 = Person("Alan", 28)
# print(p == p1)
# print(p == p2)


'''
Magic methods for comparison of various instances of same class
--> used for ordering and sorting
__lt__ --> <
__le__ --> <=
__gt__ --> >
__ge__ --> >=
__eq__ --> ==
__ne__ --> !=

You do not need to implement all of them always; 
often __eq__ + one ordering (__lt__ or __le__) is enough if you don’t sort a lot.
For real libraries, 
people sometimes use functools.total_ordering to auto-generate the rest from __eq__ + one method.
'''

# __lt__() 
# already implemented inPerson class
# print(p1 < p2) 



''' Tier 2 '''

# arithmetic operator magic methods

# __add__() --> addition operation on two object  of same type, 
# only implement when two objects can be added


class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)
  
  def __repr__(self):
    return f"Vector({self.x}, {self.y})"
  
v1 = Vector(5, 8)
v2 = Vector(6, 9)
# print(v1 + v2)

# similarly other arithmetic operators
#  __sub__()
#  __mul__()
#  __truediv__() --> for divison(/)
#  __floordev__() --> only gives quoitent(//)
#  __mod__() --> only gives remainder modulus(%)
# __pow__() --> rais to power(**)

# __contains_() --> in operator
# check whether an element belongs to a container
# if not applied python tries iteration internally but using __conatins__ is faster.


class Bag:
    def __init__(self, items):
        self.items = list(items)  # ensure it's a list

    def __bool__(self):
        return len(self.items) > 0  # True if not empty

    def __add__(self, other):
        return Bag(self.items + other.items)  # merge two bags

    def __contains__(self, item):
        return item in self.items



  
  
mybag = Bag(["apple", "banana"])
# print("apple" in mybag)
# print("mango" in mybag)


# __call__() --> make your object behave like function by making it callable.
# it is usefull in making  function like objects with state

class kounter:
  def __init__(self):
    self.count = 0

  def __call__(self):
    self.count += 1
    print("called", self.count, "times")

k = kounter()
# k()
# k()




# __enter__ and __exit__ --> Context manager(with)

# A context manager in Python is a special object designed to set up and clean up resources automatically.
# used heavily in file handling, DB concetions, locks, mutexes, transactions

class ManagedResource:
  def __enter__(self):
    print("resource acquired")
    return "Data"

  def __exit__(self, exc_type, exc_value, traceback): # always takes three positional arguments learn about more.
    print("Resource released")

with ManagedResource() as data:
  # print(data)



  
  
