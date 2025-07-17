# 🧠 OOP Concept: Hierarchical Inheritance

# ✅ Hierarchical Inheritance:
# In hierarchical inheritance, multiple derived (child) classes inherit from a single base (parent) class.
# Each child class gets access to the properties and methods of the parent class independently.

# ✅ Syntax:
# class Parent:
#     # parent methods
#
# class Child1(Parent):
#     # child1-specific methods
#
# class Child2(Parent):
#     # child2-specific methods

# ✅ Real-World Analogy:
# Think of a base class `Animal`, and child classes like `Dog`, `Cat`, and `Cow`.
# All share common properties (like breathe, eat) but also have their own behaviors.

# ✅ Use Case in Tech:
# Useful in modeling systems where different types share the same base structure.
# For example, in a UI system, all UI elements (`Button`, `TextBox`, `CheckBox`) can inherit from a common `UIElement` base class.

# -------------------------------------------------------

# ✅ Base class
class Animal:
    def sound(self):
        print("Animal makes a sound.")

# ✅ Derived class 1
class Dog(Animal):
    def bark(self):
        print("Dog says: Woof!")

# ✅ Derived class 2
class Cat(Animal):
    def meow(self):
        print("Cat says: Meow!")

# ✅ Derived class 3
class Cow(Animal):
    def moo(self):
        print("Cow says: Moo!")

# ✅ Creating objects of each derived class
dog = Dog()
cat = Cat()
cow = Cow()

# ✅ Accessing methods from base and child classes
dog.sound()
dog.bark()

print("------")

cat.sound()
cat.meow()

print("------")

cow.sound()
cow.moo()

# -------------------------------------------------------

# ✅ Summary of Hierarchical Inheritance

# 🔹 One parent → many children
# 🔹 Each child class inherits independently
# 🔹 Promotes code reuse and avoids duplication
# 🔹 Helps in organizing similar objects under a shared base

# ✅ MRO (Method Resolution Order)
# For a single base class like here, MRO is straightforward
print("MRO for Dog:", [cls.__name__ for cls in Dog.__mro__])
print("MRO for Cat:", [cls.__name__ for cls in Cat.__mro__])
print("MRO for Cow:", [cls.__name__ for cls in Cow.__mro__])
