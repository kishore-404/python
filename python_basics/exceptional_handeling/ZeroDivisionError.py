# 🧠 Exception: ZeroDivisionError

# ✅ Definition:
# ZeroDivisionError occurs when you try to divide (or modulo) a number by zero.
# Division by zero is mathematically undefined and not allowed in Python.

# ✅ When it arises:
# - Using '/' operator with zero as denominator
# - Using '//' floor division with zero denominator
# - Using '%' modulo operator with zero denominator

# ✅ Common causes:
# - User input or calculation resulting in zero denominator
# - Logical errors causing denominator to be zero
# - Forgetting to check divisor before division

# -------------------------------------------------------

def divide_numbers(a, b):
    try:
        result = a / b  # This line will raise ZeroDivisionError if b == 0
        print(f"Result of {a} / {b} is {result}")
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero!")
    else:
        print("✅ Division successful.")
    finally:
        print("🔁 Operation complete.\n")

# Test cases
divide_numbers(10, 2)  # Normal division
divide_numbers(10, 0)  # Raises ZeroDivisionError
