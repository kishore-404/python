# 🧠 File Handling: Reading One Line at a Time

def read_file_line_by_line(filename):
    try:
        # Open the file in read mode with automatic closing after block
        with open(filename, 'r') as f:
            print("File content line by line:")
            
            # Loop to read each line one by one until no more lines
            while True:
                line = f.readline()  # Read the next line from the file
                
                if not line:
                    # If line is empty (EOF), break out of the loop
                    break
                
                print(line.strip())  # Print the line after stripping newline characters
                
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
    
    print("🔁 Read operation complete.\n")

# Test
read_file_line_by_line('example.txt')
