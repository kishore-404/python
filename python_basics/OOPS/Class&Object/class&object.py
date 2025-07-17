# 🧠 OOP Concept: Class and Object

# ✅ Class:
# A class is a user-defined blueprint or prototype from which objects are created.
# It encapsulates data (attributes) and behavior (methods) into a single unit.

# ✅ Object:
# An object is an instance of a class. It holds real values and can access class methods.

# Syntax to define a class:
# class ClassName:
#     def __init__(self, parameters):
#         self.attribute = value
#     def method_name(self):
#         # code

# -------------------------------------------------------

# ✅ Defining a Class
class Person:
    # 🔸 Constructor: __init__() is automatically called when object is created.
    # self - eference to the current instance of the class.
    # __init__	Constructor for initializing objects
    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age      # instance variable

    # 🔸 Method: Function defined inside a class
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# ✅ Creating Objects (Instances) of the class
person1 = Person("Alice", 22)   # Object with name=Alice, age=22
person2 = Person("Bob", 30)     # Another object

# ✅ Accessing Method through Objects
person1.introduce()
person2.introduce()

print("------")

# -------------------------------------------------------

# ✅ Adding Behavior: More Methods in Class
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

calc = Calculator(10, 5)
print("Sum:", calc.add())
print("Product:", calc.multiply())

print("------")

# -------------------------------------------------------

# ✅ Dynamic Attributes: Add attributes outside constructor
class Animal:
    def __init__(self, species):
        self.species = species

a1 = Animal("Dog")
a1.name = "Tommy"   # Adding attribute dynamically
print("Animal:", a1.name, "-", a1.species)

print("------")

# -------------------------------------------------------

# ✅ Deleting Attributes or Objects
class Demo:
    def __init__(self, x):
        self.x = x

d = Demo(100)
print("Before delete:", d.x)

del d.x     # Delete attribute
# print(d.x)  # ❌ Will raise AttributeError

del d       # Delete object
# print(d)   # ❌ Will raise NameError

print("------")

# -------------------------------------------------------

# ✅ __str__() method: For human-readable object printing
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

b = Book("1984", "George Orwell")
print(b)  # Calls __str__ automatically

print("------")

# -------------------------------------------------------

# ✅ Summary of Class & Object Concepts

# 🔹 class: Blueprint for creating objects
# 🔹 object: Instance of a class
# 🔹 __init__: Constructor to initialize attributes
# 🔹 self: Refers to the current object instance
# 🔹 Methods: Functions inside a class
# 🔹 __str__: String representation of object
# 🔹 Dynamic attributes: Add outside class
# 🔹 del: Used to delete attributes or objects

