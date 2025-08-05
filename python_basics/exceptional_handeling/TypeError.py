# 🧠 Exception: TypeError

# ✅ Definition:
# TypeError occurs when an operation or function is applied to an object of inappropriate type.
# It means the data types of operands/arguments are incompatible for the operation.

# ✅ When it arises:
# - Trying to add incompatible types (e.g., int + str)
# - Passing wrong argument types to functions
# - Calling functions on wrong types
# - Using operators on unsupported types (like subtracting strings)

# ✅ Common causes:
# - Mixing strings and numbers in arithmetic or concatenation
# - Using list or dict methods on incompatible objects
# - Passing wrong argument types to built-in or custom functions

# -------------------------------------------------------

def add_numbers(a, b):
    try:
        result = a + b  # This may raise TypeError if a and b types mismatch
        print(f"Result of {a} + {b} is {result}")
    except TypeError:
        print("❌ Error: Unsupported operand types for + (e.g., int + str)")
    else:
        print("✅ Addition successful.")
    finally:
        print("🔁 Operation complete.\n")

# Test cases
add_numbers(5, 10)        # Works fine: int + int
add_numbers(5, "hello")   # Raises TypeError: int + str
