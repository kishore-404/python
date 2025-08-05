# 🧠 OOP Concept: Polymorphism

# ✅ What is Polymorphism?
# "Poly" means many, "morph" means forms.
# ➤ Polymorphism allows **the same method name** to perform **different behavior** depending on the object calling it.

# ➤ It's a way to use a common interface across different classes.

# ✅ Types of Polymorphism in Python:
# 1. **Duck Typing** (dynamic typing)
# 2. **Operator Overloading**
# 3. **Method Overriding** (in inheritance)

# -------------------------------------------------------

# ✅ Example 1: Duck Typing (Python’s dynamic polymorphism)

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

# Using same method 'speak()' on different objects
animal_sound(Dog())   # Woof!
animal_sound(Cat())   # Meow!

# -------------------------------------------------------

# ✅ Example 2: Method Overriding (Polymorphism with Inheritance)

class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Bike(Vehicle):
    def start(self):
        print("Kick-starting the bike...")

class Car(Vehicle):
    def start(self):
        print("Turning on car ignition...")

# Same method name, different behavior depending on the object
for v in [Vehicle(), Bike(), Car()]:
    v.start()

# -------------------------------------------------------

# ✅ Example 3: Operator Overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2      # Calls __add__()
print(p3)         # Output: (4, 6)

# -------------------------------------------------------

# ✅ Benefits of Polymorphism:
# 🔹 Promotes flexibility and reusability
# 🔹 Makes code extensible and maintainable
# 🔹 Enables generic functions and interfaces

# -------------------------------------------------------

# ✅ Common Errors:
# ❌ Not defining the same method in all subclasses
# ❌ Calling a method that doesn't exist for a given object
# ❌ Misusing operator overloading without correct return types

# -------------------------------------------------------

# ✅ Real-World Analogy:
# A person (common interface) can behave differently:
# ➤ As a teacher in a classroom,
# ➤ As a parent at home,
# ➤ As a customer in a shop.

# -------------------------------------------------------

# ✅ Summary of Polymorphism:

# 🔹 Same method name = different behavior
# 🔹 Achieved via duck typing, method overriding, and operator overloading
# 🔹 Increases code flexibility
