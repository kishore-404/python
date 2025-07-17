# 🧠 OOP Concept: Multiple Inheritance

# ✅ Multiple Inheritance:
# Multiple inheritance is a feature of object-oriented programming 
# where a class can inherit attributes and methods from more than one parent class.

# ✅ Syntax:
# class Parent1:
#     # code
# class Parent2:
#     # code
# class Child(Parent1, Parent2):
#     # inherits from both Parent1 and Parent2

# ✅ Real-World Analogy:
# A person can inherit traits from both their father and mother.
# Similarly, a class can inherit features from more than one class.

# ✅ Use Case in Tech:
# Useful when an object logically requires features from multiple distinct classes.
# Example: A `SmartPhone` class can inherit from both `Camera` and `Phone` classes.

# -------------------------------------------------------

# ✅ Parent Class 1
class Father:
    def skills(self):
        print("Father: Cooking, Driving")

# ✅ Parent Class 2
class Mother:
    def skills(self):
        print("Mother: Painting, Teaching")

# ✅ Child Class inheriting from both
class Child(Father, Mother):
    def additional_skills(self):
        print("Child: Coding")

# ✅ Creating an object of Child
c = Child()

# ✅ Accessing inherited methods
c.skills()             # Output depends on Method Resolution Order (MRO)
c.additional_skills()

print("------")

# -------------------------------------------------------

# ✅ Parent Class 1
class Artist:
    def art(self):
        print("Creates digital and physical art")

# ✅ Parent Class 2
class Engineer:
    def build(self):
        print("Designs and builds software systems")

# ✅ Child Class inheriting both
class CreativeEngineer(Artist, Engineer):
    def innovate(self):
        print("Combines art and technology for innovation")

ce = CreativeEngineer()
ce.art()       # from Artist
ce.build()     # from Engineer
ce.innovate()  # own method

print("------")

# -------------------------------------------------------

# ✅ Note on Method Resolution Order (MRO):
# Python follows the C3 Linearization Algorithm (left to right order)
# If both parents have a method with the same name, the method from the first parent is used.

# ✅ Example:
class A:
    def who(self):
        print("A")

class B:
    def who(self):
        print("B")

class C(A, B):
    pass

c = C()
c.who()  # Output: A (because A comes first in the inheritance order)

# -------------------------------------------------------

# ✅ Summary of Multiple Inheritance

# 🔹 Multiple Inheritance: One class inherits from two or more classes
# 🔹 MRO (Method Resolution Order): Determines which method is called when there's ambiguity
# 🔹 super(): Used carefully when dealing with multiple parents
# 🔹 Promotes code reusability across unrelated classes
