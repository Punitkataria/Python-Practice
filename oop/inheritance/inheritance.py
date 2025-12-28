'''
Inheritance --> when a sub class inherits or use the properties and methods of another class/superclass
helps increating relation between objects.

when to use inheritance and when to use composition:
--> use inheritance when their is an IS-A relation: Animal (parent class) --> Dog (child class)
--> use composition when their is HAS-A logic relation, not behaviour like animal and dog: Car hs a engine --> not "is-a" engine.
'''
'''
class Animal:
  def __init__(self):
    pass
  
  def sound(self):
    print("growl")

class Dog(Animal):
  def __init__(self):
    super().__init__()

  def sound(self):
    print("woof woof")

'''

'''
class Vehicle:
  def __init__(self, brand, speed):
    self.brand = brand
    self.speed = speed

class Car(Vehicle):
  def __init__(self, brand, speed):
    super().__init__(brand, speed)
    self.wheels = 4

'''
'''
class Person:
  def __init__(self, name):
    self.name = name
  
  def showinfo(self):
    print(f"Person name is {self.name}")


class Employee(Person):
  def __init__(self, name, salary):
    super().__init__(name)
    self.salary = salary

  def showinfo(self):
    super().showinfo()
    print(f"{self.name} salary is {self.salary}")

e = Employee("Alice", 25000)

print(e.name, e.salary)
'''


'''
class A:
 def f(self):
  print("A.self", self)

class B(A):
 def f(self):
  print("B.self", self)
  super().f()

class C(A):
 def f(self):
  print("C.self", self)
  super().f()

class D(C, B):
 def f(self):
  print("D.self", self)
  super().f()




d = D()
print(d.__dict__)

# thats how the MRO works 
# super function makes sure that next method in MRO is executed.
'''


# by default python use the dictionary to store attributes of an instance.
# evryt instance has two things internally one is pointer to class it belongs to and,
# second one is dictonary that stores the instance attributes.
# dictionary gives dynamic and flexible nature but have memory overhead and slower attribute access
# a python dict is a hash table with several things inhand like buckets,
# hash values, resizing logic, pointers to values and key objects
# due to this memory overhead even a small object feels heavy


# that's why slots are needed and they are fixed in size and no memory overhead 
# which makes it light and results in faster attribute access
# slots stores data contiguously which improves cpu cache usage
# read more about them later.
# do not use slots when wanted a dynamic nature, have a more complex inheritance, 
# are less flexible for meta programming, or while using ORM



class Vector:
  __slots__ = ("x", "y") # using a tuple is a standard and best choice as they are immutable and safe

  def __init__(self, x, y):
    self.x = x
    self.y = y
# tuples are more memory efficient and faster than lists to iterate.
# they perfectly aligns with slots goal for memory optimization.
# list and set are allowed but highly discouraged as they are not oriented with slots goal.
# string is never to be used as slots will parse each character as a new attribute causing mess.

import sys

v = Vector(1, 3)
# print(sys.getsizeof(v.y))


