# 🧠 Exception: ValueError

# ✅ Definition:
# ValueError occurs when a function receives an argument of the right type but an inappropriate value.
# The value itself is invalid or out of the expected range.

# ✅ When it arises:
# - Converting a string to int/float and the string is not a valid number
# - Passing invalid values to functions (e.g., math domain errors)
# - Using built-in functions or methods with inappropriate values

# ✅ Common causes:
# - Trying to convert non-numeric string to int/float
# - Using invalid parameters in functions (like invalid date formats)
# - Parsing user input without validation

# -------------------------------------------------------

def convert_to_int(value):
    try:
        num = int(value)  # Raises ValueError if value is not a valid integer string
        print(f"Conversion successful: {num}")
    except ValueError:
        print("❌ Error: Invalid literal for int() conversion.")
    else:
        print("✅ Conversion completed without errors.")
    finally:
        print("🔁 Operation complete.\n")

# Test cases
convert_to_int("123")    # Works fine
convert_to_int("abc")    # Raises ValueError
convert_to_int("12.34")  # Raises ValueError because it's not an integer literal
