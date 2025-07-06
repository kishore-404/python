# Python Set
# A set is an unordered, mutable collection of unique elements.

# Key Points:
# - Sets are unordered, so items have no index and no defined order.
# - Sets do not allow duplicate elements.
# - Sets are mutable — you can add or remove items.
# - Sets are useful for membership tests, removing duplicates, and set operations.

# Creating a set
fruits = {"apple", "banana", "cherry"}
print("Initial Set:", fruits, type(fruits))

# Adding items - add()
fruits.add("orange")           # Adds a new item
fruits.add("apple")            # Duplicate item (will be ignored)
print("After add:", fruits)

# Adding multiple items - update()
fruits.update(["kiwi", "grape"])
print("After update:", fruits)

# Removing items - remove() , discard()
fruits.remove("banana")        # Removes item (raises error if not found)
print("After remove:", fruits)

fruits.discard("mango")        # Discards item (no error if not found)
print("After discard:", fruits)

# Removing and returning a random item
popped_item = fruits.pop()
print("Popped item:", popped_item)
print("After pop:", fruits)

# Clearing the set
fruits.clear()
print("After clear:", fruits)

# Set length
print("Length of set:", len(fruits))

# Check if item exists
print("Is 'apple' in set?", "apple" in fruits)

# Loop through set
print("Looping through set:")
for fruit in {"apple", "banana", "cherry"}:
    print(fruit)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set A:", a)
print("Set B:", b)
print("Union (A | B):", a | b)
print("Intersection (A & B):", a & b)
print("Difference (A - B):", a - b)
print("Symmetric Difference (A ^ B):", a ^ b)

# Converting list to set (removing duplicates)
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Unique numbers from list:", unique_numbers)
