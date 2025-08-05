# 🧠 Exception: IndexError

# ✅ Definition:
# IndexError occurs when trying to access an index that is out of range for a sequence (like list, tuple, or string).

# ✅ When it arises:
# - Accessing a list/tuple/string with an index >= length or < -length
# - Using slicing with invalid indexes (less common, usually returns empty list)
# - Looping beyond the sequence length without proper checks

# ✅ Common causes:
# - Off-by-one errors in loops
# - Incorrect assumptions about sequence length
# - Using hardcoded indexes without validation

# -------------------------------------------------------

def access_element(seq, index):
    try:
        element = seq[index]  # May raise IndexError if index is invalid
        print(f"Element at index {index} is {element}")
    except IndexError:
        print(f"❌ Error: Index {index} is out of range for the sequence.")
    else:
        print("✅ Access successful.")
    finally:
        print("🔁 Operation complete.\n")

# Test cases
my_list = [10, 20, 30, 40]

access_element(my_list, 2)   # Valid index
access_element(my_list, 5)   # Invalid index raises IndexError
access_element(my_list, -1)  # Valid negative index
access_element(my_list, -5)  # Invalid negative index raises IndexError
