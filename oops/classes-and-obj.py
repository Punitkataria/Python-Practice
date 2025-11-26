class Person:

  # class attributes, it is shared by every instance
  counter = 0  

  # __init__ method is called automatically when a new instance is created
  def __init__(self, name, age): 
    self.name = name
    self.age = age
    Person.counter += 1

  # instance method, to call this dot notation is used
  def greet(self):
    return f"hi it's {self.name}"
  
  @classmethod
  def show_count(cls): # here cls refers to actual class
    return Person.counter
  
  @staticmethod
  def valid_age(age):
    return age >= 18
  
  

    
person1= Person("John", 18) # person1 is an instance of Person class 
# print(person1)


# Python is dynamic, means attributes can be added to an instance of class dynamically at runtime.
# person1.name = "Johnny" 
# print(person1.name)

# print(person1.greet())
# print(person1.counter)

'''
Class method --> methods that deal with class as whole not with one instance.

@class method decorator is used to create one.

A class method is meant to operate on the class itself — not on a specific object, 
that why cls is used as an argument and without it will fail.

>>> Another important reasonto use cls as an argument is to support subclasseses
as subclasses can also inherit the class method and then it will act on that subclass

why class methods exist:
--> to create objects in multiple ways, more readability, flebible, This is boggest reason for it to exist.
--> class methods can access/modify the class variables, if needed to use an instance variable here
to access the class variable then we need to create an nstncae/object first. But the whole point is to get info before object exist.
--> works good with inheritence friendly factory methods

'''
print(Person.show_count()) # here static method uses class variables and called without object

'''
static method --> method that belongs logically , even if it do ot use class or object,
it cannot receive self(instance), or cls or their data automatically,
it behaves like normal function, but it is placed logically here.

why we need them:
--> to keep related functionality together.
--> to show developer intent.
'''
# here static method is used and it can be callled using both object and class
print(person1.valid_age(20))
print(Person.valid_age(20))