'''
# message = "Hellow!"
# print(len(message))

# new_message = "Hi " + message
# print(new_message)

# is_active = True
# x = 204
# y = 104
# print(x >= y)


# Python do not support constants but to work around,
# we use all capital letters for variable name.

# FILE_SIZE_LIMT = 3000
# print(FILE_SIZE_LIMT)
# value = int(input("Enter a value: "))
# print(type(value))

# print("Divide( / ) gives full value:              5 / 2 = ",5 / 2)

# print("Floor Divide( // ) gives quoitent:         5 // 2 = ",5 // 2)

# print("Modulus operator gives the remainder:      5 % 2 = ",5 % 2)

# print("Exponentiate operator: 5 ** 2 = ",5 ** 2)

# Comparison Oeperators
# print(5 > 2)
# print(5 >= 2)
# print(5 < 2)
# print(5 <= 2)
# print(5 == 5)
# print(5 != 5)

num = 5
# print(float(num))
# print(type(str(num)))
# print(type(bool(num)))
# print(type(bool(0)))

# Ternary operator
# age = 20
# ticket_price = 20 if age >= 18 else 10
# print(ticket_price)


# always use keyword arguments for multiple parameters
# always place default parameter after the non default parameters


def greet(name, message="hi"):
  return f"{message} {name}"

print(greet("punit","hello")) # second argument is passed that's why default value is not used
print(greet("punit")) # only first argument is passed so default second argument is used



# to improve function call readability we use keyword arguments
# now during function call u do not need to specify arguments in the same order as defined in the function instead keywords are used

def get_price(price, discount):
  return price * (1-discount)

price = get_price(price=100, discount=0.1)
print(price)

'''
'''
# after the keyword argument all the argumets must also be keyword

def get_price(price, tax=0.07, discount=0.05):
  return price * (1 - discount) * (1 + tax)

print(get_price(20))

'''


# anonymous function are the function wtihout names and useful when needed to use only once. 

# lambda keyword  is used to define the anonymous function it takes parameters and only one expression.
# lambda parameters: expression

'''

# python provides a built-in function that allows to show the documentation of a function
# Docstrings
# to document your fucntion, docstrings can be used
# when the first line of the fucntion is string, python will intrepret it as a docstring.
# single or multiline strings can be add as a docstring

def add(a, b):
  "Return the sum of the two arguments"
  return a + b

print(help(add))

'''

# list unpacking

colors = ["blue", "green", "yellow"]


# we can use sequence unpacking by assigning the elements of a list to multiple variables.
# if the number of variables are fewer tan elements we will get an error.
# if we want to upack first few elements of the list  and do not care about other elements , we can
# first, unpack the needed elements to variables.
# second, pack leftover elements into a, new list  and assign it to another variable by putting asterisk(*) in fron of variable name

# red, blue, * others = colors

'''
# map() --> map function calls a function on every item of a list and return an iterator

def double(bonus):
  return bonus * 2

bonuses = [2000, 3005, 4550, 650]
new_bonuses = map(double, bonuses)
print(list(new_bonuses))

'''

'''
# filter() --> used to iterate over elements of a list and select some of them based on some criteria
scores = [70, 80, 55, 92, 43]

filtered = filter(lambda score: score >= 70, scores)
print(list(filtered))

'''

'''
# reduce() --> repeatedly apply a fucntion to an iterable to reduce it to a single value 
#  it is not built-in it lives in functools

from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, nums)
print(total)
# here it seems like lambda function takes two parameters,
# yes it is true as it do not apply to the whole list but take two pairs of values reduce them pairwise,

# It passes two arguments one is total accumulator and one is next element to be processed

'''

'''

# list comprehension --> a concise, pyhtonic way to cereate lists from anotherlists,
# ranges, strings, or any iterable
# conditions can be added in it to filter elements
# important note --> only if used than place it after for loop and if-else both are used than place them before for loop.

evens = [x for x in range(10) if x % 2 == 0]
print(evens)

labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(labels)

# flattening 2-d lists (very common)

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)



# Dictionary comprehension
squares = {x: x*x for x in range(6)}
print(squares)


# always avoid heavy logic inside comprehension as too long makes it unreadable
'''




