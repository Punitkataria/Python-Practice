'''
Decorators --> Add behaviour to fucntions or classes without modifying the actual code.

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
1. for core nuisness logic
2. if readability suffers
3. for heavy side effects
4. when orders matter a lot
5. context manager seems better option



'''