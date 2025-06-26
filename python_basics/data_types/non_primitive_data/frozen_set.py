# Python frozenset
# A frozenset is an immutable version of a set — you cannot change its elements after creation.

# Key Points:
# - frozenset is like set but immutable (no add, remove, or update).
# - Supports all read-only set operations (union, intersection, etc.).
# - Useful for use as keys in dictionaries or storing constant sets.

# Creating a frozenset
numbers = frozenset([1, 2, 3, 4])
print("Initial frozenset:", numbers, type(numbers))

# Attempting to modify (will raise AttributeError)
# numbers.add(5)          # ❌ Not allowed
# numbers.remove(2)       # ❌ Not allowed

# Read-only operations
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

print("Set A:", a)
print("Set B:", b)
print("Union (A | B):", a | b)
print("Intersection (A & B):", a & b)
print("Difference (A - B):", a - b)
print("Symmetric Difference (A ^ B):", a ^ b)

# Membership test
print("Is 2 in frozenset A?", 2 in a)

# Loop through frozenset
print("Looping through frozenset:")
for item in a:
    print(item)

# frozenset as a dictionary key
fset_key = frozenset(["apple", "banana"])
fruit_prices = {
    fset_key: 100
}
print("Dictionary with frozenset key:", fruit_prices)
