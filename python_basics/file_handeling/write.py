# 🧠 File Handling: Writing to a File

def write_to_file(filename):
    # Open the file in write mode ('w').
    # If the file does not exist, it will be created.
    # If it exists, it will be overwritten.
    with open(filename, 'w') as f:
        # Write text to the file
        f.write("Hello, this is the first line.\n")
        f.write("And this is the second line.\n")
    
    # Inform that writing is complete
    print(f"✅ Data written to '{filename}'.\n")

# Test the function
write_to_file('output.txt')
