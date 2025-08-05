# 🧠 Python Comprehensions: Syntax and Examples

# -------------------------------------------------------
# ✅ List Comprehension

# Syntax:
# new_list = [expression for item in iterable if condition]

# Example: Create a list of squares of even numbers from 0 to 9
squares = [x**2 for x in range(10) if x % 2 == 0]
print("List comprehension:", squares)
# Output: [0, 4, 16, 36, 64]

# -------------------------------------------------------
# ✅ Set Comprehension

# Syntax:
# new_set = {expression for item in iterable if condition}

# Example: Extract unique vowels from a word
vowels = {ch for ch in "comprehension" if ch in "aeiou"}
print("Set comprehension:", vowels)
# Output: {'e', 'o', 'i'}

# -------------------------------------------------------
# ✅ Dictionary Comprehension

# Syntax:
# new_dict = {key_expr: value_expr for item in iterable if condition}

# Example: Create a dictionary mapping numbers to their squares
num_dict = {x: x**2 for x in range(5)}
print("Dictionary comprehension:", num_dict)
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# -------------------------------------------------------
# ✅ Generator Comprehension

# Syntax:
# generator = (expression for item in iterable if condition)

# Example: Generator for squares of numbers
gen = (x**2 for x in range(5))
print("Generator comprehension outputs:")
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1

# -------------------------------------------------------

# ✅ Benefits of Comprehensions:
# 🔹 More readable and concise code
# 🔹 Faster to write than loops
# 🔹 Often more efficient performance-wise
