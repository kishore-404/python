# 🧠 OOP Concepts: Constructor Overloading, Destructor, and Classmethod Constructor

# -------------------------------------------------------
# ✅ 1. Constructor Overloading in Python (Pythonic Way)

# ❓ What is Constructor Overloading?
# In other languages, you can define multiple constructors with different parameters.
# Python does NOT support multiple __init__ methods, but we can achieve similar behavior using:
# 🔸 Default arguments
# 🔸 *args and **kwargs

class Book:
    def __init__(self, title="Unknown", author="Anonymous", pages=0):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print(f"📘 '{self.title}' by {self.author}, {self.pages} pages.")

# ✅ Examples of overloaded behavior:
book1 = Book("1984", "George Orwell", 328)
book2 = Book("Invisible Man", "Ralph Ellison")
book3 = Book()

book1.show_info()  # '1984' by George Orwell, 328 pages.
book2.show_info()  # 'Invisible Man' by Ralph Ellison, 0 pages.
book3.show_info()  # 'Unknown' by Anonymous, 0 pages.

print("------")

# ❌ Mistake: Trying to define multiple __init__ methods (Only last one is kept)
# class Demo:
#     def __init__(self, a): pass
#     def __init__(self, a, b): pass  # This one overrides the previous one!

# -------------------------------------------------------
# ✅ 2. Destructor (`__del__` Method)

# ❓ What is a Destructor?
# It's a special method called when an object is about to be destroyed (e.g., garbage collected).
# In Python, it's defined using `__del__`.

class TempFile:
    def __init__(self, name):
        self.name = name
        print(f"📂 Temporary file '{self.name}' created.")

    def __del__(self):
        print(f"❌ Temporary file '{self.name}' deleted.")

# ✅ Destructor is called when the object is deleted or goes out of scope
temp = TempFile("session123.txt")
del temp  # Manually deleting the object

print("------")

# ✅ Note:
# You rarely need to use destructors in Python.
# Instead, use context managers (`with` statement) or `try/finally` for cleanup.

# -------------------------------------------------------
# ✅ 3. @classmethod Constructor (Alternative Constructor)

# ❓ What is it?
# A `@classmethod` can be used to create multiple ways of instantiating a class.
# Useful for factory patterns or creating objects from other data formats.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data_string):
        # Parse string like "Alice-50000"
        name, salary = data_string.split("-")
        return cls(name, int(salary))

    def display(self):
        print(f"👤 Employee: {self.name}, Salary: ₹{self.salary}")

# ✅ Creating object using standard constructor
emp1 = Employee("Bob", 45000)

# ✅ Creating object using classmethod constructor
emp2 = Employee.from_string("Alice-60000")

emp1.display()
emp2.display()

print("------")

# -------------------------------------------------------
# ✅ Summary

# 🔹 Constructor Overloading: Use default args or *args/**kwargs (Python doesn't support method overloading)
# 🔹 Destructor: `__del__()` cleans up when object is destroyed, used rarely
# 🔹 @classmethod constructor: Alternate way to create objects (factory method pattern)
# 🔹 Use `cls` instead of `self` in classmethods

# ❗ Common Errors:
# - ❌ Overwriting multiple `__init__()` definitions
# - ❌ Forgetting to convert string to int/float in classmethod constructors
# - ❌ Assuming `__del__()` will run exactly at a known time — it's controlled by Python's garbage collector

# ✅ Best Practice:
# Use constructor for initialization
# Use classmethods for alternate ways of creating instances
# Use destructors only when necessary

