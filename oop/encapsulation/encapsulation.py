'''
Encapsulation is the core of OOP pricinple that means:
--> hide the internal details of how data is stored, and provide controlled access to it.
--> it make sure that user of class cannot misuse the data.
@property decorator --> define amtehod as a propertyor an attribute.
--> add additional logic for read, write, delete attributes by giving getter, setter, deleter method.

'''

# problem without the Encapsulation
'''
class Account:
  def __init__(self, balance):
    self.balance = balance

a = Account(500)
a.balance = -999 # illogical and wrong
print(a.balance)

# Here anyone can set garbage value which makes object invalid and have to face bugs.
# Hence we need to protect the internal attribute and provide a validated setter.
# to make readonly property, simply implement getter function property function only.
'''

class Account:
  def __init__(self, balance):
    self._balance = balance  # here value is not placed ddirectly while craeting object but by balance setter function
    # As setter is called for it.
    # The setter method of balance is responsible for updating the actual value stored in self._balance.
    
  

  @property
  def balance(self):
    return self._balance
  
  @balance.setter
  def balance(self, value):
    if value < 0:
      raise ValueError("Balance cannot be negative")
    else:
      self._balance = value


# a = Account(500)
# a.balance = -500
# print(a.balance)

# here _balance is for internal storage private by convention
# and balance is for public interface

class Rectangle:
  def __init__(self, width, height):
    self._width = width
    self._height = height

  @property
  def width(self):
    return self._width
  
  @width.setter
  def width(self, value):
    if value <= 0:
      raise ValueError("width cannot be negative or zero")
    self._width = value

  @property
  def height(self):
    return self._height
  
  @height.setter
  def height(self, value):
    if value <= 0:
      raise ValueError("height cannot be negative or zero")
    self._height = value

  @property
  def area(self):
    return self._width * self._height
  
  @property
  def perimeter(self):
    return 2 * (self._height + self._width) 
  
  def __repr__(self):
    return f"Rectangle({self._width}, {self._height})"
    

r = Rectangle(5, 9)
r.width = -2
r.height = 0


'''    

Encapsulation goal is to prevent objects from enteringinto invalid state by controlling modificatio tothe internal data.
encapsulation is pointless when constructor itself can create invalid objects.
here in above Reactangle class evrything is good but constriuctor do not check for valid values
self._height = height  --> wrong it do not check for valid values
self._width = width --> same here
to use property setter in init/constructor to validate
use-->
self.height = height
self.width = width
here python sees width and height are properties, so it calls them.
✔ validation happens
✔ Any logic in the setter is applied
✔ No invalid values can slip through
✔ Encapsulation is fully enforced

Python expands to:
--> Rectangle.width.fset(self, width)

'''
