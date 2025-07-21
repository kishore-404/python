# ✅ OOP Concept: Encapsulation
# Encapsulation is the process of bundling data (variables) and methods that operate on that data into one unit (class).
# It also restricts direct access to some of the object's components to protect the data.

# ✅ Real-Life Analogy:
# Think of a BankAccount — you can't directly touch the money inside a bank system.
# You interact with it using deposit(), withdraw(), and get_balance() methods.

# ✅ Class using Encapsulation
class BankAccount:
    # Constructor to initialize account owner and balance
    def __init__(self, owner, balance):
        self.owner = owner              # Public attribute: can be accessed directly
        self.__balance = balance        # 🔒 Private attribute: cannot be accessed directly outside the class

    # ✅ Getter method to read the balance (controlled access)
    def get_balance(self):
        return self.__balance           # Accessing the private variable safely

    # ✅ Setter method to update the balance (controlled update)
    def set_balance(self, new_balance):
        if new_balance >= 0:            # Validation check
            self.__balance = new_balance
        else:
            print("❌ Balance cannot be negative!")

    # ✅ Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited ₹{amount}")
        else:
            print("❌ Invalid deposit amount")

    # ✅ Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrawn ₹{amount}")
        else:
            print("❌ Insufficient balance!")

# ✅ Creating an object of BankAccount
account = BankAccount("John Doe", 5000)

# ✅ Accessing public attribute
print("Account Owner:", account.owner)

# ❌ Accessing private attribute directly will raise error (Not Recommended)
# print(account.__balance)  # Uncommenting this line would cause AttributeError

# ✅ Accessing private data through methods (encapsulation in action)
print("Current Balance:", account.get_balance())  # Getter

# ✅ Updating balance through setter
account.set_balance(6000)
print("Updated Balance:", account.get_balance())

# ✅ Depositing money
account.deposit(1500)

# ✅ Withdrawing money
account.withdraw(2000)

# ❌ Trying to withdraw more than the balance
account.withdraw(10000)

# ✅ Final balance check
print("Final Balance:", account.get_balance())
