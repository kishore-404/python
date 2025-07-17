# 🧠 OOP Concept: Hybrid Inheritance

# ✅ Hybrid Inheritance:
# Hybrid Inheritance is a combination of two or more types of inheritance in a single program.
# It may include single, multiple, multilevel, and/or hierarchical inheritance in any combination.

# ✅ Syntax:
# class A: ...
# class B(A): ...
# class C: ...
# class D(B, C): ...

# ✅ Real-World Analogy:
# Imagine a Student who is both a SchoolMember (single inheritance), 
# and also inherits behavior from both Person and Learner classes (multiple inheritance).
# This forms a hybrid structure.

# ✅ Use Case in Tech:
# Useful when designing large systems with shared traits.
# Example: In a content platform, `User` class could inherit from both `Profile` and `Subscription`,
# while still being part of a larger `Person` hierarchy.

# -------------------------------------------------------

# ✅ Base Class
class Person:
    def info(self):
        print("Person: Has a name and age.")

# ✅ Intermediate Class - Single Inheritance from Person
class Student(Person):
    def student_info(self):
        print("Student: Attends school or college.")

# ✅ Another Base Class
class Sports:
    def sports_info(self):
        print("Sports: Plays a sport.")

# ✅ Derived Class - Multiple Inheritance (Hybrid structure)
class SchoolAthlete(Student, Sports):
    def athlete_info(self):
        print("SchoolAthlete: Is a student who plays sports.")

# ✅ Create object
sa = SchoolAthlete()

# ✅ Accessing all inherited and own methods
sa.info()          # From Person
sa.student_info()  # From Student
sa.sports_info()   # From Sports
sa.athlete_info()  # From SchoolAthlete

print("------")

# -------------------------------------------------------

# ✅ Another Example: Combining Hierarchical + Multiple Inheritance

# Base class
class Vehicle:
    def category(self):
        print("Vehicle: Base class")

# Derived from Vehicle (1st level)
class Car(Vehicle):
    def car_type(self):
        print("Car: 4-wheeler")

# Another class not derived from Vehicle
class Electric:
    def battery(self):
        print("Electric: Uses battery")

# Derived from both Car and Electric — Hybrid
class Tesla(Car, Electric):
    def brand(self):
        print("Tesla: Electric car brand")

t = Tesla()
t.category()    # From Vehicle
t.car_type()    # From Car
t.battery()     # From Electric
t.brand()       # Own method

# -------------------------------------------------------

# ✅ Summary of Hybrid Inheritance

# 🔹 Combines multiple types of inheritance in one structure
# 🔹 Enables code reuse across various class hierarchies
# 🔹 Method Resolution Order (MRO) is important to resolve ambiguity
# 🔹 Use `super()` carefully when constructors are involved in hybrid trees

# ✅ Tip:
# To see MRO of a class: print(ClassName.__mro__)
print("Method Resolution Order:", [cls.__name__ for cls in Tesla.__mro__])
    