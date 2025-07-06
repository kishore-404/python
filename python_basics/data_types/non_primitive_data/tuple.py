# Python Tuple
# A tuple is an ordered, immutable collection that can store multiple items, including duplicates.

# Key Points:
# - Tuples are ordered: items have a defined order and can be accessed by index.
# - Tuples are immutable: once created, you cannot change, add, or remove items.
# - Tuples allow duplicate elements.
# - Tuples can contain elements of different data types.


# Creating and Accessing Elements
# Length and Membership
# Looping and Slicing
# Single Item and Mixed Data Types
# Nested Tuples and Accessing Nested Items
# Conversion Between List and Tuple
# Count and Index Methods
# Unpacking and Extended Unpacking
# Using Tuples as Dictionary Keys
# Returning Multiple Values from Functions
# Named Tuples for Immutable Records
# Immutability Benefits
# Concatenation and Repetition
# Sorting with Tuples by Multiple Criteria


# Creating a tuple
fruits = ("apple", "banana", "cherry")
print("Initial Tuple:", fruits, type(fruits))

# Access elements by index (zero-based)
print("First element:", fruits[0])
print("Last element:", fruits[-1])

# Tuple length
print("Length of tuple:", len(fruits))

# Check if item exists
print("Is 'apple' in tuple?", "apple" in fruits)

# Loop through tuple
print("Looping through tuple:")
for fruit in fruits:
    print(fruit)

# Slicing tuples (subtuple)
print("Slice fruits[0:2]:", fruits[0:2])

# Tuple with one item (important syntax)
single_item = ("apple",)
print("Single item tuple:", single_item, type(single_item))

# Tuple can contain mixed data types
mixed_tuple = ("apple", 42, True, 3.14)
print("Mixed type tuple:", mixed_tuple)

# Nested tuple
nested = ("apple", ("banana", "cherry"))
print("Nested tuple:", nested)
print("Access nested item:", nested[1][0])

# Converting between list and tuple
fruits_list = list(fruits)      # Convert to list to modify
fruits_list.append("orange")    
fruits = tuple(fruits_list)     # Convert back to tuple
print("Modified tuple (via list):", fruits)
    
# Count and index
print("Count of 'apple':", fruits.count("apple"))
print("Index of 'cherry':", fruits.index("cherry"))

# 1. Tuple unpacking (multiple assignment)
a, b, c = ("apple", "banana", "cherry")
print(a, b, c)

# 2. Extended unpacking with *
a, *b, c = (1, 2, 3, 4, 5)
print(a, b, c)  # a=1, b=[2,3,4], c=5

# 3. Using tuples as dictionary keys (immutability makes them hashable)
my_dict = {("x", "y"): 10}
print(my_dict[("x", "y")])

# 4. Returning multiple values from functions via tuples
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 7, 2, 9])
print(low, high)

# 5. Named tuples for readable, immutable record-like structures (from collections)
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)

# 6. Immutability benefits: thread-safety and integrity guarantees

# 7. Concatenation and repetition (creates new tuples)
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)
t4 = t1 * 3
print(t4)

# 8. Using tuples in sorting: sort list of tuples by multiple criteria
data = [("apple", 2), ("banana", 1), ("cherry", 3)]
data.sort(key=lambda x: x[1])
print(data)