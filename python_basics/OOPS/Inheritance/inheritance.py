# ------------------------------------------------------------
# 🧠 Object-Oriented Programming: Inheritance in Python
# ------------------------------------------------------------

# ✅ What is Inheritance?
# Inheritance is an OOP concept where one class (child) inherits 
# the attributes and methods of another class (parent).
# It promotes reusability and logical hierarchy.

# ✅ Real-World Analogy:
# A Car is a type of Vehicle.
# All cars have wheels, engines (from Vehicle class),
# but also have specific features (like sunroof) of their own.

# ✅ Why Use Inheritance in Tech?
# - Code Reusability: Avoid repeating code in similar classes.
# - Extensibility: Easily extend base classes for new features.
# - Maintainability: Common functionality in one base place.
# - Polymorphism: Same interface, different implementation.

# ✅ Syntax of Inheritance:
# class ChildClass(ParentClass):
#     def __init__(self):
#         super().__init__()  # To call ParentClass's constructor

# ------------------------------------------------------------
# ✅ Example: Single Inheritance
# ------------------------------------------------------------

# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} engine started.")

# Derived class
class Car(Vehicle):  # Inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand)  # Call Vehicle's constructor
        self.model = model

    def display_info(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Create object of derived class
car1 = Car("Toyota", "Camry")
car1.start_engine()       # Inherited from Vehicle
car1.display_info()       # Own method
