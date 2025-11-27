class Person: # by convention capitalised names are used for classes

  # class attributes, it is shared by every instance and they can be created dynamically at runtime.
  counter = 0  

  # __init__ method is called automatically when a new instance is created
  def __init__(self, name, age, sex): 
    self.name = name
    self.age = age
    self.sex = sex
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
  
  

    
person1= Person("John", 18, "male") # person1 is an instance of Person class 
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
# print(person1.valid_age(20))
# print(Person.valid_age(20))


'''
Most important concept to know:

A class is also an object as all others, when a class is defined,
python internally creates a object, its name can be found using __name__ attribute.
now that class also ahve a type and behaviour to craete new instance.
Every class in pyhton that we craete are an instance of class "type"
'''
# print(Person.__name__)
# print(type(Person))

'''
Dynamic Attribute Management
'''

# setattr() function creates value dynamically at runtime
# setattr(person1, "male_count", 0)
# print(person1.male_count)

# hasattr() function checks if an attribute exist or not 
# print(hasattr(person1, "male_count"))

# getattr() get value dynamically
# value = getattr(person1, "age")
#print(value)

# delattr() delete value at runtime
# delattr(person1, "male_count")


'''
Private and Proctected attributes are conventions not forced like c++/java.
'''

# Proctected attribute
class Boy:
  def __init__(self, age):
    self._age = age

b = Boy(12)
print(b._age) # stll gives result but highly discouraged

# Private attribute

class Girl:
  def __init__(self, age):
    self.__age = age

g = Girl(15)
print(g.__age)  # gives Attribute error
print(g._Girl__age) # possible but discouraged
# prevent accidental overiding
# protect developer intent