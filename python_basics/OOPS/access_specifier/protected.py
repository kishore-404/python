# 🧠 OOP Concept: Access Specifiers - Protected

# ✅ What are Protected Members?

# ➤ Protected members are **intended to be accessed only within the class** and its **subclasses**.
# ➤ They are *not truly private*, but signal that they shouldn’t be used outside unless necessary.
# ➤ Python uses **a single underscore `_`** before the member name.

# 🔸 Syntax:
# self._variable  ← protected variable
# def _method():  ← protected method

# -------------------------------------------------------

# ✅ Example of Protected Members

class Employee:
    def __init__(self, name, salary):
        self.name = name              # 🔹 public
        self._salary = salary         # 🟡 protected

    def show_info(self):
        print(f"Employee: {self.name}, Salary: ₹{self._salary}")

# ✅ Subclass accessing protected member
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}, Dept: {self.department}, Salary: ₹{self._salary}")

# ✅ Creating objects
emp1 = Employee("Anita", 40000)
mgr1 = Manager("Suresh", 60000, "IT")

# ✅ Accessing protected member (⚠️ not recommended outside class/subclass)
print(emp1._salary)        # ⚠️ Works, but should be avoided
mgr1.show_manager_info()   # ✅ Works inside subclass

# -------------------------------------------------------

# ✅ Summary: Protected Members

# 🟡 Starts with single underscore: `_salary`
# 🟡 Intended for internal use — accessible in class & subclasses
# 🟡 Python doesn’t enforce it, but it’s a **convention**
# 🟡 Use when child classes need access, but external access should be discouraged

# -------------------------------------------------------

# ⚠️ Real-World Analogy:
# Protected = like a manager's internal files — only managers (child classes) and HR (parent class) should view them.

# -------------------------------------------------------

# 🔍 Common Mistake:
# ❌ Using `_` to mean private. It’s **not private**.
# ✅ You *can* access it outside the class, but **shouldn’t unless needed**.

# -------------------------------------------------------

# ✅ All Access Levels Summary:

# | Access Type | Prefix | Outside Access | Subclass Access |
# |-------------|--------|----------------|------------------|
# | Public      | none   | ✅ Yes         | ✅ Yes           |
# | Protected   | `_`    | ⚠️ Avoid       | ✅ Yes           |
# | Private     | `__`   | ❌ No          | ❌ No            |

# -------------------------------------------------------

# 🚀 You’ve now completed **Access Specifiers**!



