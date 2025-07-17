# 🧠 OOP Concept: Inheritance (Multilevel Inheritance)

# ✅ Multilevel Inheritance:
# Multilevel inheritance is a form of inheritance where a class is derived from a class 
# which is also derived from another class.
# In simple terms, a child class inherits from a parent, and then another child inherits from that child.

# Syntax:
# class Base:
#     # base class
# class Derived1(Base):
#     # intermediate class
# class Derived2(Derived1):
#     # final class

# ✅ Real-World Analogy:
# Think of it like this:
#     Grandparent ➝ Parent ➝ Child
#     Traits and behaviors can be passed down through generations.

# -------------------------------------------------------

# ✅ Base Class (Grandparent)
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print(f"I am a {self.species}")

# ✅ Derived Class (Parent)
class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)  # Call Animal constructor
        self.breed = breed

    def bark(self):
        print(f"{self.breed} is barking!")

# ✅ Further Derived Class (Child)
class Puppy(Dog):
    def __init__(self, species, breed, age):
        super().__init__(species, breed)  # Call Dog constructor
        self.age = age

    def info(self):
        print(f"This is a {self.age}-month-old {self.breed} puppy.")

# ✅ Creating an object of the last derived class
puppy1 = Puppy("Canine", "Labrador", 5)

# ✅ Accessing methods from all 3 levels
puppy1.speak()  # from Animal
puppy1.bark()   # from Dog
puppy1.info()   # from Puppy

print("------")

# -------------------------------------------------------

# ✅ Summary of Multilevel Inheritance

# 🔹 Multilevel Inheritance: Inheriting in a chain-like fashion (A ➝ B ➝ C)
# 🔹 super(): Used to call constructor/method from immediate parent
# 🔹 Promotes: Reusability across a longer inheritance chain
# 🔹 Object: Has access to all methods and attributes from ancestors
