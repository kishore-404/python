# 🧠 Python Concept: Decorators

# ✅ Definition:
# A decorator is a function that takes another function as input,
# adds some functionality to it, and returns a new function.
# Decorators help modify behavior of functions or methods dynamically.

# ✅ Why we need decorators:
# 🔹 Code reuse (add common functionality like logging, timing, authentication)
# 🔹 Separation of concerns (keep core logic clean)
# 🔹 Enhance or modify existing functions without changing their code

# -------------------------------------------------------

# ✅ Syntax:

# A simple decorator function:
def decorator_func(original_func):
    def wrapper_func():
        print("Before the original function runs.")
        original_func()
        print("After the original function runs.")
    return wrapper_func

# Using decorator by manual assignment:
def say_hello():
    print("Hello!")

say_hello = decorator_func(say_hello)
say_hello()

# -------------------------------------------------------

# ✅ Preferred Syntax: Using '@' decorator syntax
@decorator_func
def greet():
    print("Greetings!")

greet()


