# Non-Primitive Data Types 
# These data types can store multiple values and are built using primitive types.
# They are used to structure and organize data.

# Key Points:
# Non-primitive types can store a collection of values.
# They can be mutable (like list, dict, set) or immutable (like tuple).
# They allow for complex data structures.

# List - ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry"]
print("List:", fruits, type(fruits))

# Tuple - ordered, immutable, allows duplicates
coordinates = (10.5, 20.3)
print("Tuple:", coordinates, type(coordinates))

# Set - unordered, mutable, no duplicates
unique_numbers = {1, 2, 3, 4}
print("Set:", unique_numbers, type(unique_numbers))

# Dictionary - unordered (insertion ordered as of Python 3.7+), mutable, key-value pairs
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print("Dictionary:", student, type(student))

# Custom Class / Object - user-defined complex data type
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

my_car = Car("Toyota", 2022)
print("Custom Object:", my_car.brand, my_car.year, type(my_car))
