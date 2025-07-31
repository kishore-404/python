# 🧠 OOP Concept: Constructor in Python

# ✅ What is a Constructor?
# A constructor in Python is a special method named `__init__`.
# It automatically runs when you create a new object from a class.
# It is used to initialize (set) the attributes of a class.

# ✅ Syntax:
# class ClassName:
#     def __init__(self, parameters):
#         self.attribute = parameter

# ✅ Real-world Analogy:
# Think of a constructor like a registration form that collects data as soon as an object is created.
# Without it, every object would start blank.

# -------------------------------------------------------

# ✅ Example Class with Constructor
class Person:
    def __init__(self, name, age):
        # Constructor is called when a new Person object is created
        self.name = name    # assign name to the instance
        self.age = age      # assign age to the instance

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# ✅ Creating an object automatically calls the constructor
person1 = Person("Alice", 25)
person1.greet()  # Output: Hello, my name is Alice and I am 25 years old.

print("------")

# -------------------------------------------------------

# ✅ Benefits of Constructor:
# 🔹 Automatically initializes data when an object is created
# 🔹 Reduces manual setup after creating objects
# 🔹 Improves code readability and structure
# 🔹 Useful for dependency injection or required setup tasks

# -------------------------------------------------------

# ❌ Common Mistakes and Errors:

# ❌ 1. Missing required arguments when creating an object
# person2 = Person()  # ❌ TypeError: __init__() missing 2 required positional arguments

# ❌ 2. Forgetting `self` in __init__ method
# class Animal:
#     def __init__(species):      # ❌ Missing self
#         self.species = species  # ❌ Will raise NameError

# ✅ Correct way:
# class Animal:
#     def __init__(self, species):
#         self.species = species

# ❌ 3. Assigning to wrong variable name (typo)
# def __init__(self, name):
#     self.nam = name  # ❌ Now self.name is undefined

# -------------------------------------------------------

# ✅ Advanced: Constructor with Default Parameters

class Student:
    def __init__(self, name="Unknown", grade="Not Assigned"):
        self.name = name
        self.grade = grade

    def show(self):
        print(f"Student: {self.name}, Grade: {self.grade}")

# Even if no values are passed, defaults will be used
s1 = Student()
s2 = Student("Tom", "A")

s1.show()  # Student: Unknown, Grade: Not Assigned
s2.show()  # Student: Tom, Grade: A

print("------")

# -------------------------------------------------------

# ✅ Summary of Constructor in Python

# 🔹 __init__ is the constructor method in Python
# 🔹 Automatically called when an object is created
# 🔹 Used to initialize attributes of the class
# 🔹 Accepts parameters to customize each object
# 🔹 Always has `self` as the first parameter
# 🔹 Can have default values
# 🔹 Errors may occur if arguments are missing or `self` is misused
