# Python List
# A list is an ordered, mutable collection that can store multiple items, including duplicates.

# Key Points:
# - Lists are ordered, meaning items have a defined order and can be accessed by index.
# - Lists are mutable, so you can change, add, or remove items after creation.
# - Lists allow duplicate elements.
# - Lists can contain elements of different data types.

# Python List Basics
# Creating and Inspecting Lists
# Accessing List Elements by Index
# Modifying List Elements (Mutability)
# Adding Elements to a List
# Removing Elements from a List
# List Length and Membership Check
# Looping Through a List
# Slicing Lists (Sublists)
# Sorting Lists
# Copying Lists
# Clearing Lists
# List Comprehensions
# Filtering Lists with List Comprehensions
# Nested Lists (Lists of Lists)
# Extended List Methods: extend(), count(), index()
# Using enumerate() to Get Index and Value
# Sorting with Custom Key Functions
# List Unpacking with *
# Using deque for Efficient Double-Ended Operations


# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Initial List:", fruits, type(fruits))

# Access elements by index (zero-based)
print("First element:", fruits[0])
print("Last element:", fruits[-1])

# Change an element (mutability)
fruits[1] = "blueberry"
print("After modification:", fruits)

# Add elements
fruits.append("orange")          # Add to the end
print("After append:", fruits)

fruits.insert(1, "kiwi")         # Add at specific position
print("After insert:", fruits)

# Remove elements
fruits.remove("kiwi")            # Remove by value
print("After remove:", fruits)

popped_item = fruits.pop()       # Remove and return last item
print("Popped item:", popped_item)
print("After pop:", fruits)

del fruits[0]                    # Delete by index
print("After del:", fruits)

# List length
print("Length of list:", len(fruits))

# Check if item exists
print("Is 'apple' in list?", "apple" in fruits)

# Loop through list
print("Looping through list:")
for fruit in fruits:
    print(fruit)

# Slicing lists (sublist)
print("Slice fruits[1:3]:", fruits[1:3])

# Sorting
fruits.sort()                    # Sorts in-place (alphabetically)
print("After sort:", fruits)

sorted_fruits = sorted(fruits)   # Returns a new sorted list
print("Sorted copy:", sorted_fruits)

# Reverse list
fruits.reverse()                 # Reverses list in-place
print("After reverse:", fruits)

# Copy list
fruits_copy = fruits.copy()
print("Copied list:", fruits_copy)

# Clear list
fruits.clear()
print("After clear:", fruits)

# 1. List Comprehension: Create a new list by applying an expression to each item in an iterable
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Filter with list comprehension: Include only items meeting a condition
even_squares = [x for x in squares if x % 2 == 0]
print("Even squares:", even_squares)


# 2. Nested Lists: Lists that contain other lists (like a matrix or grid)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:", matrix)
print("Element at row 2, col 3:", matrix[1][2])  # 6


# 3. Extended List Methods:
nums = [1, 2, 3, 4, 2, 2, 5]

# extend(): Add multiple items at once to the end of a list
nums.extend([6, 7])
print("After extend:", nums)

# count(): Count how many times a value appears in the list
count_twos = nums.count(2)
print("Number of 2's:", count_twos)

# index(): Find the first index of a value in the list
first_two_index = nums.index(2)
print("First index of 2:", first_two_index)


# 4. enumerate(): Get index and value when looping over a list
print("Enumerate example:")
for index, value in enumerate(nums):
    print(f"Index {index}: Value {value}")


# 5. Sorting with key: Customize how the list is sorted by giving a key function
words = ["apple", "banana", "pear", "kiwi", "orange"]

# Sort by length of the word
words.sort(key=len)
print("Words sorted by length:", words)

# Sort by last letter of the word
sorted_by_last_letter = sorted(words, key=lambda w: w[-1])
print("Words sorted by last letter:", sorted_by_last_letter)


# 6. List Unpacking: Assign list items to variables easily, including grabbing multiple items with *
values = [10, 20, 30, 40, 50]

a, b, *rest = values
print("a:", a)
print("b:", b)
print("rest:", rest)

first, *middle, last = values
print("first:", first)
print("middle:", middle)
print("last:", last)


# 7. deque: A double-ended queue for fast adding/removing from both ends (better than list for these)
from collections import deque
dq = deque([1, 2, 3])

dq.appendleft(0)   # add to the front
dq.append(4)       # add to the end
print("Deque after appends:", dq)

dq.popleft()       # remove from the front
dq.pop()           # remove from the end
print("Deque after pops:", dq)
