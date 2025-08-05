# 🧠 Python Concept: File Handling

# ✅ Definition:
# File Handling allows you to create, read, write, and manipulate files stored on your computer.
# It lets programs persist data, exchange information, and work with large datasets.

# ✅ Why We Need File Handling:
# 🔹 To save data permanently (beyond program execution)
# 🔹 To read input or configuration files
# 🔹 To log application activity or errors
# 🔹 To exchange data between programs or systems

# ✅ Common File Modes:
# 'r'  - Read (default), file must exist
# 'w'  - Write, creates or truncates file
# 'a'  - Append, adds to end of file
# 'x'  - Create, fails if file exists
# 'b'  - Binary mode (add with other modes, e.g. 'rb')
# 't'  - Text mode (default)

# ✅ Syntax:

# Open a file:
# file = open('filename', 'mode')

# Read or write:
# file.read(), file.readline(), file.write()

# Close the file:
# file.close()

# Better way using `with` statement (auto closes file):
# with open('filename', 'mode') as file:
#     # work with file

# -------------------------------------------------------

# ✅ Example: Writing to and Reading from a file

def write_file():
    with open('example.txt', 'w') as f:  # Open file in write mode
        f.write("Hello, world!\n")
        f.write("Welcome to file handling in Python.\n")
    print("✅ Data written to file.\n")

def read_file():
    try:
        with open('example.txt', 'r') as f:  # Open file in read mode
            content = f.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("❌ Error: File not found.")
    print("🔁 Read operation complete.\n")

# Test file handling functions
write_file()
read_file()

# -------------------------------------------------------

# ✅ Benefits of File Handling:
# 🔹 Data persistence beyond program lifecycle
# 🔹 Large data storage and retrieval
# 🔹 Interaction with external systems or users

# -------------------------------------------------------

# ⚠️ Limitations / Considerations:
# ❌ File corruption risk if program crashes during write
# ❌ File access permissions can cause errors
# ❌ Must manage file closing to avoid memory leaks (use 'with' to avoid this)
