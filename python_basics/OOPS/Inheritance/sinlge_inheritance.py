# 🧠 OOP Concept: Inheritance (Single Inheritance)

# ✅ Inheritance:
# Inheritance is a feature of object-oriented programming that allows a class (child class)
# to inherit properties and behaviors (methods and attributes) from another class (parent class).
# It promotes code reusability and hierarchical classification.

# ✅ Single Inheritance:
# Single Inheritance means one child class inherits from one parent class.

# Syntax:
# class Parent:
#     def __init__(self):
#         # constructor
#     def method(self):
#         # method

# class Child(Parent):
#     def __init__(self):
#         super().__init__()  # Call parent constructor
#     def another_method(self):
#         # child-specific logic

# -------------------------------------------------------

# ✅ Parent Class
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.color} {self.brand} vehicle is starting...")

# ✅ Child Class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, color, model):
        # 🔸 Call parent constructor using super()
        super().__init__(brand, color)
        self.model = model

    def display_info(self):
        print(f"This is a {self.color} {self.brand} {self.model} car.")

# ✅ Creating an object of the Child Class
my_car = Car("Toyota", "Red", "Camry")

# ✅ Access methods from both child and parent
my_car.display_info()   # Method from Car
my_car.start()          # Inherited method from Vehicle

print("------")

# -------------------------------------------------------

# ✅ Explanation of super():
# `super()` is used to refer to the parent class.
# It allows you to call the parent constructor or methods without explicitly naming the parent.

# ✅ Real-World Analogy:
# Think of a Vehicle as a general category (base class), and a Car is a specific type of vehicle (subclass).
# The Car inherits common features like 'start' from Vehicle and can have its own unique features.

# -------------------------------------------------------

# ✅ Summary of Single Inheritance

# 🔹 Inheritance: Mechanism to reuse parent class code
# 🔹 Parent Class: The class being inherited from
# 🔹 Child Class: The class that inherits from the parent
# 🔹 super(): Refers to the parent and is used to access its methods/constructor
# 🔹 Promotes: Code reusability, extensibility, and clean structure
