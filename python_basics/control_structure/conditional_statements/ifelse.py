# Python If-Else Control Structures
# Used to control the flow of logic based on conditions (boolean expressions)

# 1. Simple if statement
# Executes the block only if the condition is True
x = 10
if (x > 0):
    print("x is positive")

# 2. if-else statement
# Chooses between two blocks of code
x = -5
if (x >= 0):
    print("x is non-negative")
else:
    print("x is negative")

# 3. if-elif-else ladder
# Useful when checking multiple exclusive conditions
score = 85
if (score >= 90):
    print("Grade: A")
elif (score >= 80):
    print("Grade: B")
elif (score >= 70):
    print("Grade: C")
elif (score >= 60):
    print("Grade: D")
else:
    print("Grade: F")

# 4. Nested if statements
# You can nest if-else blocks inside other if-else blocks
age = 20
has_id = True

if (age >= 18):
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry denied: Underage")

# 5. Short-hand if (also called "ternary" or "conditional expression")
x = 5
result = "Even" if( x % 2 == 0) else "Odd"
print("Number is", result)

# 6. Multiple conditions using 'and' / 'or'
temperature = 25
humidity = 70

if temperature > 20 and humidity > 60:
    print("It might feel humid and warm")

if temperature < 15 or humidity < 50:
    print("Either cool or dry climate")

# 7. Using 'in' with if
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")

# 8. Using 'not' in condition
if not fruits:
    print("Fruit list is empty")
else:
    print("Fruit list has items")

# Summary of Python conditional types:
# - if
# - if-else
# - if-elif-else
# - nested if
# - short-hand if
# - logical conditions with and/or/not
# - membership check using in / not in
