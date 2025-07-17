# 🧠 Python Input Methods
# Python offers several ways to accept input from the user or other sources.

# --------------------------------------------------------
# 1️⃣ Basic input() function
# Takes input as a string from the user via console

name = input("Enter your name: ")  # Always returns a string
print("Hello,", name)

# Convert to int or float if needed
age = int(input("Enter your age: "))     # Convert string to int
price = float(input("Enter price: "))    # Convert string to float
print("Age:", age, "| Price:", price)

print("-----")

# --------------------------------------------------------
# 2️⃣ Multiple values in one line using split()
# Useful when accepting space-separated values

x, y = input("Enter two numbers: ").split()
x = int(x)
y = int(y)
print("Sum:", x + y)

# Or: read multiple and store in a list
nums = list(map(int, input("Enter numbers: ").split()))
print("Numbers List:", nums)

print("-----")

# --------------------------------------------------------
# 3️⃣ Using *args-like behavior to collect all inputs
# You can use unpacking to take variable number of inputs

*a, = input("Enter any number of values: ").split()
print("Values:", a)

print("-----")

# --------------------------------------------------------
# 4️⃣ Fast input using sys.stdin (for large input or competitive coding)

import sys
data = sys.stdin.readline().strip()  # Reads one line including \n
print("You entered:", data)

# Uncomment this for actual use in terminals:
# for line in sys.stdin:
#     print("Line:", line.strip())

print("-----")

# --------------------------------------------------------
# 5️⃣ Command-line arguments using sys.argv
# These are inputs passed when you run the script from the command line

# Example run: python script.py apple 123
import sys
print("Script name:", sys.argv[0])     # First element is always the script name
print("Arguments passed:", sys.argv[1:])  # Rest are user-passed args

print("-----")

# --------------------------------------------------------
# 6️⃣ Reading from a file using open()

# Assume there's a file named 'data.txt' with some content
# Uncomment to use:
# with open('data.txt', 'r') as file:
#     content = file.read()
#     print("File content:\n", content)

print("-----")

# --------------------------------------------------------
# 7️⃣ Using fileinput to support stdin or file input

# import fileinput
# for line in fileinput.input():
#     print("Line from input or file:", line.strip())

print("-----")

# --------------------------------------------------------
# 8️⃣ GUI-based input using Tkinter (optional for GUI apps)

# from tkinter import *
# def show_input():
#     print("User Input:", entry.get())
# root = Tk()
# entry = Entry(root)
# entry.pack()
# Button(root, text="Submit", command=show_input).pack()
# root.mainloop()

print("-----")

# 🧾 Summary of Input Types:

# - input()               → Console input (string)
# - int(), float(), etc.  → Convert input to other types
# - split(), map(), list  → Handle multiple values at once
# - sys.stdin             → Faster input for large data
# - sys.argv              → Command-line input
# - open(), fileinput     → File or stream input
# - GUI input             → For apps (Tkinter, etc.)

# 🟡 Tip: input() always returns a **string**, so use type conversion when needed.
