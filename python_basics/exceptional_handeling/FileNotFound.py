# 🧠 Exception: FileNotFoundError

# ✅ Definition:
# FileNotFoundError occurs when trying to open or access a file that does not exist at the specified path.

# ✅ When it arises:
# - Using `open()` on a non-existent file in read mode
# - Trying to read from or write to a file path that is invalid or inaccessible
# - Incorrect file path or filename

# ✅ Common causes:
# - Typos in file name or path
# - File deleted or moved
# - Relative vs absolute path mistakes
# - Permissions issues (less common for this error, usually permission denied)

# -------------------------------------------------------

def read_file(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"❌ Error: File '{filepath}' not found.")
    else:
        print("✅ File read successfully.")
    finally:
        print("🔁 Operation complete.\n")

# Test cases
read_file('existing_file.txt')   # Replace with a file you know exists
read_file('missing_file.txt')    # File that does not exist
