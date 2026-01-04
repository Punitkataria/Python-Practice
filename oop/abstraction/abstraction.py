'''
Abstraction -->  is a design principle where code depends on behviour, 
not on concrete implementaionexposing what a thing does, hiding how it does it.

user --> knows the capabilities and do not care about implementation
creator --> free to change internals and must respect the contract

Python uses abstraction and polymorphism far more than inheritance.
Abstraction can be implemented via 4 mechanisms in python:
--> functions
--> abstract base class(ABC) 
--> protocols/duck typing(typing.Protocol)
--> composition over inheritance

why python is called "protocol based"?
because even without protocols or ABC, python:
1. uses implicit protocols everywhere
2. dispatches behaviour based on method presence
3. rarely checks class identity

So protocols match python's nature, ABC adds guardrails.

Yes — both protocols and ABCs implement abstraction, 
but protocols do it by describing behavior, 
while ABCs do it by enforcing contracts through inheritance.
'''

'''
# Functional Abstraction (foundational) --> whenever we use funciton we already using abstracton as caller 
# only needed to know what function to use, what it does and what parameter it takes 
# but doesn't need to know the working of function.

def send_email(to, subject, body):
  # hidden implementation
  print("connecting to SMTP server")
  print("sending email")

send_email("user@email.com", "hi", "hello")
'''

'''
# class based aabstraction (naive) --> 
# before python had abc and protocols, developers still needed a common shape, shared api,
# and a base class to talk about "what a thing is supposed to do".
# This is the simplest form of abstraction
# use it in small internal projects, quick prototypes, legacy code

class PaymentProcessor:
  def pay(self, amount):
    raise NotImplementedError("subclasses must implement pay()")
  
class Stripe(PaymentProcessor):
  def pay(self, amount):
    print(f"paid {amount} using stripe")

class Paypal( PaymentProcessor):
  def pay(self, amount):
    print(f"paid {amount} using paypal")

def checkout(processor: PaymentProcessor, amount):
  processor.pay(amount)

# here checkout depends on what pay not how
checkout(Stripe(), 5000)
checkout(Paypal(), 1000)
'''

'''
Explicit Protocols(Behaviour based abstraction)
--> declared description of behaviour that an object must have without requiring inheritance,
it makes duck typing visible and checkable.

from typing import Protocol

# this means any object that hase write(str) -> None is a Logger.
class Logger(Protocol):
  def write(self, msg:str) -> None:
    pass

# no base class and no inheritance
class FileLogger:
  def write(self, msg:str) -> None:
    print(f"file: {msg}")

class SocketLogger:
  def write(Self, msg:str) -> None:
    print(f"socket: {msg}")

# using the prortocol
def process(logger: Logger):
  logger.write("Processing started")

process(SocketLogger())

# depends on behaviour, hides implemenation and repacable componenets
# any logger that do not implements write() does not will give runtime AttributeError
# python will not block this but type checker will do
# so protocols are design time safety.
'''


# Abstarct Base Class(Contract-Based abstraction)
# An ABC --> a base class that enforces the contract at runtime using inheritance,which makes it stronger but less flexible.

# defining An  ABC

from abc import ABC, abstractmethod

class Logger(ABC):
  @abstractmethod
  def write(Self, msg: str) -> None:
    pass
# you must implement write to be a logger

class FileLogger(Logger):
  def write(self, msg: str) -> None:
    print(f"File: {msg}")

# using ABC

def process(logger: Logger):
  logger.write("processing")

process(FileLogger())

# enforcement at runtime whenever using a logger that do not implement write will give TypeError
# here same abstraction is implemeneted but more strict contract

# Protocols describe behaviour and ABC enforces it
# Pyhton favours Protocols more






