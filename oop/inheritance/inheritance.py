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


print(D.__mro__)

d = D()
print(d.f())

  
# thats how the MRO works 
# super function makes sure that next method in MRO is executed.
  
