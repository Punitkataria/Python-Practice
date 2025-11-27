'''
Magic or dunder or doubleunderscore methods make the objects behave like python built types.
Why magic methods matters ?
Because they let us make custom classes behave like lists, dicts,number, functions, iterators, context manager

'''

# __init__ () --> object initializer, called right after the object is created, it initilise the instance attributes

class Person:
  def __init__(self, name , age):
    self.name = name
    self.age = age 

p = Person("Alice", 25)
print(p.name, p.age)