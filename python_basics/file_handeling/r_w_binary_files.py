# 🧠 File Handling: Reading and Writing Binary Files

def write_binary_file(filename):
    # Open file in binary write mode ('wb')
    with open(filename, 'wb') as f:
        # Write bytes data to the file
        data = b'\x00\xFF\x10\x20'  # Example byte sequence
        f.write(data)
    print(f"✅ Binary data written to '{filename}'.\n")

def read_binary_file(filename):
    # Open file in binary read mode ('rb')
    try:
        with open(filename, 'rb') as f:
            data = f.read()  # Read all bytes
            print(f"Binary data read from '{filename}': {data}")
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    print("🔁 Binary read operation complete.\n")

# Test
write_binary_file('binaryfile.bin')
read_binary_file('binaryfile.bin')
