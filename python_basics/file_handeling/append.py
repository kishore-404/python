# 🧠 File Handling: Appending to a File

def append_to_file(filename):
    # Open the file in append mode ('a').
    # If the file does not exist, it will be created.
    # If it exists, new data will be added at the end.
    with open(filename, 'a') as f:
        # Write additional text to the file
        f.write("This line is appended.\n")
        f.write("Appending more lines is easy!\n")
    
    # Inform that appending is complete
    print(f"✅ Data appended to '{filename}'.\n")

# Test the function
append_to_file('output.txt')
