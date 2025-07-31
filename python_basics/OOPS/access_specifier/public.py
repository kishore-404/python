# 🧠 OOP Concept: Access Specifiers - Public

# ✅ What is an Access Specifier?
# Access specifiers (or access modifiers) define the visibility/scope of class members (variables/methods).
# Python supports 3 access levels:
# 1️⃣ Public
# 2️⃣ Protected
# 3️⃣ Private

# -------------------------------------------------------

# ✅ 1️⃣ Public Members

# ➤ Public members are accessible from **anywhere** — inside or outside the class.
# ➤ No special symbol is needed; all members are public by default.

# 🔸 Syntax:
# class MyClass:
#     def __init__(self):
#         self.name = "Public Member"  # public variable

# -------------------------------------------------------

# ✅ Example of Public Members

class Student:
    def __init__(self, name, grade):
        self.name = name        # 🔹 public attribute
        self.grade = grade      # 🔹 public attribute

    def display_info(self):     # 🔹 public method
        print(f"Student: {self.name}, Grade: {self.grade}")

# ✅ Object creation
student1 = Student("Alice", "A")

# ✅ Accessing public members outside the class
print(student1.name)        # ✅ Works: Alice
print(student1.grade)       # ✅ Works: A
student1.display_info()     # ✅ Works: Student: Alice, Grade: A

# -------------------------------------------------------

# ✅ Summary: Public Members

# 🔹 No underscore prefix (`name`)
# 🔹 Accessible from anywhere (inside/outside the class)
# 🔹 Default visibility for all class members in Python
# 🔹 Suitable for data you want to exp
