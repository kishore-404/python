# 🧠 OOP Concept: Access Specifiers - Private

# ✅ What are Private Members?

# ➤ Private members are **only accessible within the class** they are defined in.
# ➤ They **cannot be accessed directly from outside** the class.
# ➤ Python uses **double underscores `__`** as a naming convention to indicate private.

# 🔸 Syntax:
# self.__variable  ← private variable
# def __method():  ← private method

# -------------------------------------------------------

# ✅ Example of Private Members

class BankAccount:
    def __init__(self, name, balance):
        self.name = name                # 🔹 public
        self.__balance = balance        # 🔒 private

    def show_balance(self):            # 🔹 public method
        print(f"Hello {self.name}, your balance is ₹{self.__balance}")

    def __secret_method(self):         # 🔒 private method
        print("This is a secret method!")

# ✅ Object creation
account1 = BankAccount("Ravi", 5000)

# ✅ Accessing public method
account1.show_balance()  # ✅ Hello Ravi, your balance is ₹5000

# ❌ Accessing private variable directly (outside class)
# print(account1.__balance)        # 🔴 AttributeError

# ❌ Accessing private method directly
# account1.__secret_method()       # 🔴 AttributeError

# ✅ Correct way to access private variable (using name mangling)
print(account1._BankAccount__balance)      # ✅ Works, but not recommended (₹5000)

# ✅ Correct way to access private method (not recommended)
account1._BankAccount__secret_method()     # ✅ Works, but breaks encapsulation

# -------------------------------------------------------

# ✅ Summary: Private Members

# 🔐 Starts with double underscores: `__balance`
# 🔐 Not accessible directly from outside
# 🔐 Used for sensitive data: passwords, pin, internal logic
# 🔐 Can be accessed (but **not recommended**) using name mangling: `_ClassName__member`

# -------------------------------------------------------

# ⚠️ Real-World Analogy:
# Think of private members like your **ATM PIN** — only you (the class) should use it, not others.

# -------------------------------------------------------

# 🔍 Common Mistakes:

# ❌ Trying to access private variables directly:
#    print(obj.__privateVar)  → AttributeError
# ✅ Always use getter/setter or public methods to interact safely

# -------------------------------------------------------

# 🚀 Next: Type `next` to move to **Protected Members**
