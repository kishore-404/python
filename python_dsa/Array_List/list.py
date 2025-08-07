# ✅ Definition:
# A list in Python is a **built-in, ordered, mutable** data structure.
# It is similar to dynamic arrays in other languages (like ArrayList in Java or Vector in C++).
# Lists can hold items of **different data types**, including other lists.

# ✅ Why we use Lists:
# 🔹 Store multiple values in a single variable
# 🔹 Efficient access and update via index (O(1) time)
# 🔹 Dynamic in size — no need to declare fixed capacity
# 🔹 Rich set of built-in methods for easy manipulation (append, remove, sort, etc.)

# -------------------------------------------------------

# ✅ Syntax & Basic Operations:

# Create a list
my_list = [10, 20, 30, 40, 50]

# Access elements
print(my_list[0])   # Output: 10
print(my_list[-1])  # Output: 50 (last element)

# Update an element
my_list[2] = 35

# Append a new element
my_list.append(60)

# Insert at specific index
my_list.insert(1, 15)

# Remove element by value
my_list.remove(35)

# Remove and return last element
last = my_list.pop()

# Find length of list
print(len(my_list))  # Output: 5

# -------------------------------------------------------

# ✅ Iterating through a list

for element in my_list:
    print(element)

# Using index
for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")

# -------------------------------------------------------

# ✅ List Comprehension

squares = [x*x for x in range(6)]  # [0, 1, 4, 9, 16, 25]

evens = [x for x in my_list if x % 2 == 0]

# -------------------------------------------------------

# ✅ Common Built-in Methods:

my_list = [1, 5, 2, 9, 1, 5]

print(my_list.count(5))   # Count how many times 5 appears
print(my_list.index(2))   # Find the index of 2
my_list.sort()            # Sort the list
my_list.reverse()         # Reverse the list
my_list.clear()           # Remove all elements

# -------------------------------------------------------

# ✅ Explanation:
# - Lists are stored in **contiguous memory locations**
# - Indexing is fast (O(1)), but inserting/removing in the middle is slower (O(n))
# - Append() is amortized O(1); insert(), remove(), pop(index) are O(n)
# - Python lists grow dynamically in memory when needed

# -------------------------------------------------------

# ✅ Benefits:
# 🔸 Very flexible and easy to use
# 🔸 Dynamic memory management (no size declaration needed)
# 🔸 Powerful built-in tools and methods
# 🔸 Can hold heterogeneous data

# -------------------------------------------------------

# ✅ Limitations:
# ❌ Slower than low-level arrays (like numpy or C arrays) for numeric computation
# ❌ Inserting/removing in the middle requires shifting elements (O(n))
# ❌ Takes more memory (each element stores type info & pointers)

# -------------------------------------------------------

# ✅ When to use Lists:
# 🔹 When you need an ordered, mutable collection
# 🔹 When index-based access is important
# 🔹 When size is unknown or changes frequently
