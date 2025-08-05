# 🧠 Handling Multiple Exceptions

# ✅ Why:
# Sometimes a code block can raise different kinds of exceptions.
# Handling multiple exceptions lets you manage each error type separately or together.

# ✅ Syntax options:

# Option 1: Separate except blocks for different exceptions
try:
    # risky operations
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("❌ Error: Invalid input, not a number.")
except ZeroDivisionError:
    print("❌ Error: Division by zero is not allowed.")
else:
    print(f"✅ Result is {y}")
finally:
    print("🔁 Operation finished.\n")

# Option 2: Single except block catching multiple exceptions
try:
    x = int(input("Enter a number: "))
    y = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f"❌ Error: {e}")
else:
    print(f"✅ Result is {y}")
finally:
    print("🔁 Operation finished.\n")
