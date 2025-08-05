# 🧠 Exception: KeyError

# ✅ Definition:
# KeyError occurs when trying to access a dictionary key that does not exist.

# ✅ When it arises:
# - Accessing a non-existent key in a dictionary using `dict[key]`
# - Using `pop()` or other methods with a missing key (without default)
# - Incorrect assumptions about dictionary contents

# ✅ Common causes:
# - Typos in key names
# - Missing keys due to incomplete data
# - Not checking if a key exists before access

# -------------------------------------------------------

def access_dict_key(d, key):
    try:
        value = d[key]  # May raise KeyError if key not found
        print(f"Value for key '{key}': {value}")
    except KeyError:
        print(f"❌ Error: Key '{key}' not found in dictionary.")
    else:
        print("✅ Access successful.")
    finally:
        print("🔁 Operation complete.\n")

# Test cases
my_dict = {'name': 'Alice', 'age': 25}

access_dict_key(my_dict, 'name')    # Valid key
access_dict_key(my_dict, 'address') # Invalid key, raises KeyError
