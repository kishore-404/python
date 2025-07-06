# Python Functions
# A function is a reusable block of code that performs a specific task , when its called.

# ~ Definition: You define a function using the 'def' keyword.
# ~ Parameters: Functions can take arguments (inputs).
# ~ Return: Functions can return values using the 'return' keyword.
# ~ Reusability: Write once, use many times.
# ~ Abstraction: Helps organize code logically.

# 1. Simple function definition and call
def greet(): {
    # This function simply prints a greeting message
    print("Hello, welcome to Python functions!")
}
# Call the function
greet()

print("-----")

# 2. Function with parameters
def greet_user(name):{
    # 'name' is a parameter; it's a placeholder for input
    print(f"Hello, {name}!")  #f"" -  formatted string 
}
# Call function with argument
greet_user("Alice")

print("-----")

# 3. Function with multiple parameters and return value
def add(a, b):
    # This function takes two numbers and returns their sum
    return a + b

# Call the function and store the result
result = add(5, 3)
print("Sum:", result)

print("-----")

# 4. Function with default parameters
def power(base, exponent=2):
    # Exponent defaults to 2 if not provided
    return base ** exponent

print("Square of 4:", power(4))         # uses default exponent=2
print("4 to the power of 3:", power(4, 3))  # overrides default

print("-----")

# 5. Function returning multiple values (tuple)
def calculate(a, b):
    # Returns sum and difference of two numbers
    return a + b, a - b

s, d = calculate(10, 4)
print("Sum:", s)
print("Difference:", d)

print("-----")

# 6. Keyword arguments and positional arguments
def info(name, age):
    print(f"Name: {name}, Age: {age}")

info("Bob", 25)                    # Positional
info(age=30, name="Charlie")      # Keyword arguments (order doesn't matter)

print("-----")

# 7. Variable-length arguments using *args and **kwargs
def show_items(*args):
    # *args lets you pass any number of positional arguments
    for item in args:
        print("Item:", item)

show_items("pen", "book", "eraser")

print("-----")

def show_profile(**kwargs):
    # **kwargs lets you pass any number of keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_profile(name="Alice", age=22, city="New York")

print("-----")

# 8. Anonymous (lambda) function
# Small, one-line function without using def
square = lambda x: x * x
print("Square of 5 using lambda:", square(5))

print("-----")

# 9. Nested function
def outer():
    print("Inside outer function")

    def inner():
        print("Inside inner function")

    inner()  # Call inner function inside outer

outer()

print("-----")

# 10. Function Scope
x = 10  # Global variable

def show_scope():
    x = 5  # Local variable
    print("Inside function:", x)
    print("from Inside function acces glabal var:", globals()['x'])

show_scope()
print("Outside function:", x)  # Global x remains unchanged


# Use  globals()['x'] dictionary to access the global variable explicitly
# Summary of Function Types and Concepts:
# - Simple function: No parameters
# - Function with parameters and return
# - Default arguments
# - Return multiple values
# - Positional & keyword arguments
# - *args: variable-length positional
# - **kwargs: variable-length keyword
# - lambda: anonymous function
# - Nested functions
# - Variable scope: local vs global
