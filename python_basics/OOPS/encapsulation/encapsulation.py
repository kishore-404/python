# 🧠 OOP Concept: Encapsulation

# ✅ What is Encapsulation?
# Encapsulation is the concept of **bundling data (attributes) and methods** that operate on the data
# into a single unit (class), and **restricting access to some of the object's components**.
# This prevents direct modification of internal states and protects object integrity.

# ➤ Encapsulation hides internal details and only exposes a controlled interface.
# ➤ In Python, encapsulation is implemented using:
#    - Private variables (using double underscores `__`)
#    - Getter and Setter methods (@property decorators)

# -------------------------------------------------------

# ✅ Example: Encapsulation using private attributes and getter/setter

class Employee:
    def __init__(self, name, salary):
        self.name = name               # public
        self.__salary = salary         # private

    # Getter method (access salary safely)
    @property
    def salary(self):
        return self.__salary

    # Setter method (update salary with validation)
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative!")
        else:
            self.__salary = value

    def display(self):
        print(f"Employee: {self.name}, Salary: ₹{self.__salary}")

# ✅ Using encapsulation
emp = Employee("Raj", 50000)
emp.display()                   # Employee: Raj, Salary: ₹50000

# ❌ Direct access to private variable (will cause error)
# print(emp.__salary)           # AttributeError

# ✅ Access using getter
print(emp.salary)               # 50000

# ✅ Update salary using setter
emp.salary = 60000
print(emp.salary)               # 60000

# ❌ Invalid update using setter
emp.salary = -1000              # Salary cannot be negative!
print(emp.salary)               # 60000 (unchanged)

# -------------------------------------------------------

# ✅ Summary: Encapsulation

# 🔐 Hides internal data from outside access
# 🔐 Use private variables to store data securely
# 🔐 Provide getter and setter methods for controlled access/modification
# 🔐 Helps prevent accidental or unauthorized changes to object state
# 🔐 Enhances modularity, security, and maintainability

# -------------------------------------------------------

# ⚠️ Common Mistakes

# ❌ Directly accessing private variables (`obj.__var`) → AttributeError
# ❌ No validation logic in setters → Data inconsistency
# ✅ Always use property decorators to validate before updating

# -------------------------------------------------------

# ✅ Real-World Analogy:
# Think of encapsulation like a **capsule pill** — medicine inside is protected and only released in the right way.

# -------------------------------------------------------

# 🚀 Next up: Polymorphism (method overriding & operator overloading)
