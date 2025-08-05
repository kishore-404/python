# 🧠 OOP Concept: Data Abstraction

# ✅ Definition:
# Data Abstraction is the process of hiding internal details and showing only the essential features of an object.
# In Python, this is often done using abstract base classes and abstract methods from the `abc` module.

# ✅ Why We Need Abstraction:
# 🔹 To hide complex implementation details from the user
# 🔹 To enforce a standard interface across all subclasses
# 🔹 To focus only on what an object does, not how it does it
# 🔹 Helps in designing secure, maintainable, and modular code

# ✅ Syntax:
# - Use the `abc` module
# - Create an abstract base class using `ABC`
# - Define abstract methods using the `@abstractmethod` decorator
# - Subclasses must implement all abstract methods to be instantiated

# -------------------------------------------------------

# ✅ Example Code: Data Abstraction in action

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

# Concrete subclass implementing abstract methods
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")

    def stop_engine(self):
        print("Bike engine stopped.")

# Function that uses abstraction — works with any Vehicle
def operate(vehicle):
    vehicle.start_engine()
    print("...Driving...")
    vehicle.stop_engine()

# Creating objects
c = Car()
b = Bike()

# ✅ Works because both classes implement abstract methods
operate(c)
# Output:
# Car engine started.
# ...Driving...
# Car engine stopped.

operate(b)
# Output:
# Bike engine started.
# ...Driving...
# Bike engine stopped.

# -------------------------------------------------------

# ✅ Benefits of Data Abstraction:
# 🔹 Hides complexity and exposes only essentials
# 🔹 Forces implementation of required methods (interface enforcement)
# 🔹 Promotes code reusability and cleaner design
# 🔹 Helps manage large codebases by defining clear contracts

# -------------------------------------------------------

# ⚠️ Limitations / Considerations:
# ❌ Can't instantiate abstract classes directly
# ❌ All abstract methods must be implemented in child class
# ❌ May increase complexity in very small projects

# Example of limitation:
# v = Vehicle()  # ❌ TypeError: Can't instantiate abstract class Vehicle with abstract methods

# -------------------------------------------------------

# ✅ Summary:
# 🔸 Data Abstraction hides the 'how' and exposes only the 'what'
# 🔸 Achieved using abstract base classes and methods in Python
# 🔸 Useful for enforcing structure, reducing complexity, and building scalable systems
