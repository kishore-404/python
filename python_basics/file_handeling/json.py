import json

# 🧠 File Handling: Working with JSON Files

# ✅ Definition:
# JSON (JavaScript Object Notation) is a lightweight data interchange format.
# Python’s `json` module allows reading/writing JSON data from/to files easily.

# -------------------------------------------------------

def write_json_file(filename, data):
    # Open file in write mode
    with open(filename, 'w') as f:
        # Serialize 'data' as JSON and write to file
        json.dump(data, f, indent=4)  # indent=4 makes file pretty formatted
    print(f"✅ JSON data written to '{filename}'.\n")

def read_json_file(filename):
    try:
        # Open file in read mode
        with open(filename, 'r') as f:
            # Load JSON data from file and convert to Python object
            data = json.load(f)
            print("JSON data read from file:")
            print(data)
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    print("🔁 JSON read operation complete.\n")

# -------------------------------------------------------

# Sample Python dictionary (can be any serializable Python object)
sample_data = {
    "name": "Alice",
    "age": 30,
    "languages": ["English", "Spanish", "French"],
    "is_student": False
}

# Test writing and reading JSON
write_json_file('data.json', sample_data)
read_json_file('data.json')
