# 🧠 OOP Concept: Duck Typing

# ✅ Definition:
# Duck Typing is a concept where the type of an object is determined by its behavior (methods),
# not by its actual class. If an object implements the needed method, it can be used regardless of its type.

# ✅ Syntax:
# Just call a method on an object without checking its type.
# Python will execute it as long as the method exists.

# -------------------------------------------------------

# ✅ Example Code: Duck Typing in action

class Duck:
    def speak(self):
        print("Quack!")

class Human:
    def speak(self):
        print("Hello!")

# A function that accepts any object with a 'speak()' method
def call_speak(entity):
    entity.speak()  # No type check; we trust that 'speak()' exists

# Creating different objects
d = Duck()
h = Human()

# ✅ Works because both have a 'speak()' method
call_speak(d)  # Output: Quack!
call_speak(h)  # Output: Hello!

# -------------------------------------------------------

# ✅ Benefits of Duck Typing:
# 🔹 Flexible and dynamic — no need to check types explicitly
# 🔹 Encourages generic and reusable code
# 🔹 Reduces code coupling (less dependency on specific classes)
# 🔹 Works well with polymorphism

# -------------------------------------------------------

# ⚠️ Limitations of Duck Typing:
# ❌ Errors occur at runtime if the expected method is missing
# ❌ No compile-time safety (typos or missing methods won't be caught early)
# ❌ Can be harder to debug in large systems

# Example of limitation:
class Tree:
    def grow(self):
        print("Growing...")

t = Tree()
call_speak(t)  # ❌ AttributeError: 'Tree' object has no attribute 'speak'

# -------------------------------------------------------

# ✅ Summary:
# 🔸 Duck Typing relies on behavior, not type
# 🔸 "If it walks like a duck and quacks like a duck, it’s a duck"
# 🔸 Powerful in dynamic languages like Python, but needs careful usage
