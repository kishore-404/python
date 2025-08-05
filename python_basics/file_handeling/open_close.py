# 🧠 File Handling Step 1: Opening and Closing a File

# ✅ Definition:
# Opening a file means creating a connection between your program and the file stored on disk.
# Closing a file means terminating that connection and freeing resources.

# ✅ Syntax:
# file = open('filename', 'mode')
# file.close()

# -------------------------------------------------------

# Example:

try:
    file = open('sample.txt', 'w')  # Open file in write mode
    file.write("This is a sample line.\n")
    print("✅ Data written to file.")
finally:
    file.close()  # Important to close the file
    print("🔁 File closed.\n")
