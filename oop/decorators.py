'''
Decorators --> Add behaviour to fucntions or classes without modifying the actual code.
A decorator is a callable that takes a function and returns a new function.

Think of decorators as compile time funciton transformers.

Important note: Decorators run at import time because they are executed as part of function definition,
not function invocation.

First principle: how Python executes a module

1. Creates a module object
2. Executes the module top-to-bottom
3. Stores names in the module's namespace

There is no “compile then run later” separation like in C/Java.


Use --> 
1. when the mdification is not the aprt of core business logic and applied to many functions.
examples are logging, authentication/autherization. caching, rate limiting, input validation and more.
2. when repetetive and generic behviour is needed to applied.

when not to use -->
1. for core buisness logic
2. if readability suffers
3. for heavy side effects
4. when orders matter a lot
5. context manager seems better option
'''


# what actauly happening behind
import time
from datetime import datetime, timedelta

# here we are trying to do a process and also calculating time 
# but if need to do the same for every other process we will be voileting the dry principle. 
# we will use a decorator that will extend any process fucntionality and return a function.
'''

def brew_tea():
  # here we are brewing tea but also calculating time
  
  start = time.time()
  print("brewing tea....")
  time.sleep(1)
  print("tea is brewed")
  end = time.time()
  print(f"task time: {end - start}")

brew_tea()

'''
'''
def timer_dec(base_func):
  def enhanced_func():
    start_time = time.time()
    base_func()
    end_time = time.time()
    print(f"time taken: {end_time - start_time}")
  return enhanced_func

def brew_tea():
  print("brewing tea...")
  time.sleep(1)
  print("tea is ready")

# applying decorator

time_brewing = timer_dec(brew_tea)
time_brewing() 

# here what happend is we seperated the time calculation logic from tea process logic 
# and this time calculation logic can be applied to any other process but it behaves like same when we mixed both

# also isntead of calling decoartor directly we can use @ symbol above any function to use decorator with

@timer_dec
def make_matcha():
  print("making matcha...")
  time.sleep(1)
  print("matacha is ready")

# now instead of calling the decorator we can directly call the fucntion and the decorator is appled on it 
# using @ symbol is just syntactic sugar as internally decorator is called with this make_matcha fucntion

'''

# decoarating functions with parameters
# we need to pass parameters when defining a decorator to both base_func and and returned func


def timer_dec(base_func):
  # *args is used to make it accept any number of arguments
  # if we want our base func to return than we need to store base func result and return it in enhanced func 
  # it makes the decorator flexible
  def enhanced_func(*args):
    start_time = time.time()
    result = base_func(*args)
    end_time = time.time()
    print(f"time taken: {end_time - start_time}")
    return result
  return enhanced_func



@timer_dec
def brew_tea(tea_type, steep_time):
  print(f"brewing {tea_type} tea...")
  time.sleep(steep_time)
  print("tea is ready")
  return f"drink by {datetime.now() + timedelta(minutes=30)}"

@timer_dec
def make_matcha():
  print("making matcha...")
  time.sleep(1)
  print("matacha is ready")
  return f"drink by {datetime.now() + timedelta(minutes=30)}"


print(brew_tea("green", 3))
print(make_matcha()) 

# here this function can also be used with timer decorator as the decorator can take any number of arguents
# **kwargs can also be used to give any number of keyword arguments