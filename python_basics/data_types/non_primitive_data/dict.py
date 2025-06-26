# Python Dictionary
# A dictionary is an unordered, mutable collection of key-value pairs.

# Key Points:
# - Dictionaries store data as key-value pairs.
# - Keys must be unique and immutable (e.g., strings, numbers, tuples).
# - Values can be of any data type and can be duplicated.
# - Dictionaries are mutable — you can add, update, or remove items.

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Initial Dictionary:", person, type(person))

# Accessing values by key
print("Name:", person["name"])
print("Age:", person.get("age"))  # Safer way to access (returns None if key doesn't exist)

# Adding or updating items
person["email"] = "alice@example.com"   # Add new key
person["age"] = 31                      # Update existing key
print("After additions/updates:", person)

# Removing items
person.pop("city")             # Remove by key
print("After pop:", person)

del person["email"]            # Delete by key using `del`
print("After del:", person)

# Loop through dictionary
print("Keys:")
for key in person:
    print(key)

print("Values:")
for value in person.values():
    print(value)

print("Key-Value pairs:")
for key, value in person.items():
    print(key, "=>", value)

# Check if key exists
print("Is 'name' in dictionary?", "name" in person)

# Dictionary length
print("Number of items:", len(person))

# Copying a dictionary
person_copy = person.copy()
print("Copied dictionary:", person_copy)

# Clearing the dictionary
person.clear()
print("After clear:", person)

# Nested dictionary
student = {
    "name": "John",
    "grades": {
        "math": 85,
        "science": 90
    },
    "active": True
}
print("Nested dictionary:", student)
print("Math grade:", student["grades"]["math"])
