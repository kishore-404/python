# 🧠 OOP Concept: Operator Overloading

# ✅ Definition:
# Operator Overloading allows **built-in operators** (like +, -, *, ==) to have **custom behavior**
# based on the **class of the objects** involved.
# You can redefine what an operator does by defining special methods (also called magic methods or dunder methods).

# ✅ Syntax:
# Define special methods like:
# 🔸 __add__() → for +
# 🔸 __sub__() → for -
# 🔸 __mul__() → for *
# 🔸 __eq__() → for ==
# 🔸 __lt__() → for <
# 🔸 __str__() → for string representation

# -------------------------------------------------------
# ✅ Example: Overloading the + and == operators

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overload the '+' operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overload the '==' operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # For printing
    def __str__(self):
        return f"({self.x}, {self.y})"

# Creating two Point objects
p1 = Point(2, 3)
p2 = Point(4, 1)

# Using overloaded + operator
p3 = p1 + p2
print(p3)  # Output: (6, 4)

# Using overloaded == operator
print(p1 == p2)  # Output: False
print(p1 == Point(2, 3))  # Output: True

# -------------------------------------------------------

# ✅ Benefits of Operator Overloading:
# 🔹 Makes custom classes behave like built-in types
# 🔹 Improves readability and usability of objects
# 🔹 Enables mathematical operations with user-defined types

# -------------------------------------------------------

# ⚠️ Limitations:
# ❌ Misusing operator overloading can make code hard to understand
# ❌ Must be used meaningfully — don't override + to do something confusing
# ❌ Can lead to unexpected bugs if not implemented carefully

# -------------------------------------------------------

# ✅ Summary:
# 🔸 Operator Overloading gives custom meaning to built-in operators for your objects
# 🔸 Uses special methods like __add__, __eq__, __str__, etc.
# 🔸 Helps write intuitive, clean, and Pythonic class interfaces
