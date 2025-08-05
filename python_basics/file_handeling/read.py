# 🧠 File Handling : Reading a File

# ✅ Definition:
# Reading a file means accessing and retrieving the contents stored in the file.

# ✅ Important:
# File must exist in 'read' ('r') mode, or Python raises FileNotFoundError.

# ✅ Ways to read:
# - read(): reads entire content as a single string
# - readline(): reads one line at a time
# - readlines(): reads all lines and returns a list of lines

# -------------------------------------------------------

def read_entire_file(filename):
    # Try-except block to handle possible file not found error
    try:
        # 'with' keyword automatically opens the file and closes it after the block finishes
        # 'open(filename, 'r')' opens the file in read mode ('r')
        # 'as f' assigns the opened file object to variable 'f'
        with open(filename, 'r') as f:
            # Read the entire content of the file and store it in variable 'content'
            content = f.read()  
            
            # Print the content read from the file
            print("File content:")
            print(content)
    except FileNotFoundError:
        # If the file does not exist, this block runs
        print(f"❌ Error: File '{filename}' not found.")
    
    # This runs regardless of error or not
    print("🔁 Read operation complete.\n")

# Call the function with a filename
read_entire_file('example.txt')