# 🧠 Python: *args vs **kwargs

# ✅ *args (Non-keyword Variable-Length Arguments):
# - Collects extra positional arguments passed to a function into a tuple.
# - Useful when you want to accept any number of positional arguments.

def example_args(*args):
    print("Received positional arguments (args):", args)
    for i, arg in enumerate(args):
        print(f"Argument {i}: {arg}")

example_args(1, 2, 3)
# Output:
# Received positional arguments (args): (1, 2, 3)
# Argument 0: 1
# Argument 1: 2
# Argument 2: 3

# -------------------------------------------------------

# ✅ **kwargs (Keyword Variable-Length Arguments):
# - Collects extra keyword arguments (named arguments) into a dictionary.
# - Useful when you want to accept any number of named arguments.

def example_kwargs(**kwargs):
    print("Received keyword arguments (kwargs):", kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

example_kwargs(name="Alice", age=30, city="New York")
# Output:
# Received keyword arguments (kwargs): {'name': 'Alice', 'age': 30, 'city': 'New York'}
# name = Alice
# age = 30
# city = New York

# -------------------------------------------------------

# ✅ Using *args and **kwargs together:

def example_both(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)

example_both(10, 20, name="Bob", job="Developer")
# Output:
# Positional args: (10, 20)
# Keyword args: {'name': 'Bob', 'job': 'Developer'}
