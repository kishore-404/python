# Python List
# A list is an ordered, mutable collection that can store multiple items, including duplicates.

# Key Points:
# - Lists are ordered, meaning items have a defined order and can be accessed by index.
# - Lists are mutable, so you can change, add, or remove items after creation.
# - Lists allow duplicate elements.
# - Lists can contain elements of different data types.

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
