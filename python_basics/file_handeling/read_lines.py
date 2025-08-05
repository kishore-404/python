# 🧠 File Handling: Reading All Lines at Once using readlines()

def read_file_with_readlines(filename):
    try:
        # Open file in read mode; file auto-closed after block
        with open(filename, 'r') as f:
            # readlines() reads all lines into a list where each line is an element
            lines = f.readlines()
            
            print("File content as list of lines:")
            for line in lines:
                print(line.strip())  # Print each line after removing newline characters
                
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    
    print("🔁 Read operation complete.\n")

# Test
read_file_with_readlines('example.txt')
