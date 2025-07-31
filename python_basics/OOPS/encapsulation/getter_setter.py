# 🧠 OOP Concept: Getters and Setters (Accessors and Mutators)

# ✅ What are Getters and Setters?

# ➤ Getters: Methods that retrieve (get) the value of a private attribute.
# ➤ Setters: Methods that set (modify) the value of a private attribute, often with validation.
# ➤ They enforce **controlled access** to private variables while hiding implementation details.

# ➤ In Python, the idiomatic way to create getters and setters is using the `@property` decorator.

# -------------------------------------------------------

# ✅ Example: Using @property decorators

class Student:
    def __init__(self, name, marks):
        self.name = name            # public
        self.__marks = marks        # private

    # Getter method to access __marks
    @property
    def marks(self):
        return self.__marks

    # Setter method to set __marks with validation
    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            print("Invalid marks! Must be between 0 and 100.")
        else:
            self.__marks = value

# ✅ Usage
student = Student("Meera", 85)

# ✅ Access marks using getter
print(student.marks)           # 85

# ✅ Modify marks using setter
student.marks = 95
print(student.marks)           # 95

# ❌ Try invalid value
student.marks = 150            # Invalid marks! Must be between 0 and 100.
print(student.marks)           # 95 (unchanged)

# ❌ Direct access to private variable fails
# print(student.__marks)       # AttributeError

# -------------------------------------------------------

# ✅ Summary: Getters and Setters

# 🔹 Use `@property` to create a getter
# 🔹 Use `@<property_name>.setter` to create a setter
# 🔹 Provide validation inside setters to protect data integrity
# 🔹 They allow attribute access syntax (`obj.attr`) but still control the underlying data

# -------------------------------------------------------

# ⚠️ Common Mistakes:

# ❌ Forgetting to use setter — attribute becomes read-only
# ❌ Not validating data in setter — leads to invalid internal state
# ❌ Accessing private attribute directly instead of using getter/setter

# -------------------------------------------------------

# ✅ Real-World Analogy:

# Think of getters/setters like a thermostat:
# You can read the temperature (getter), and set a new temperature (setter) — but the thermostat checks if the setting is safe.

# -------------------------------------------------------

