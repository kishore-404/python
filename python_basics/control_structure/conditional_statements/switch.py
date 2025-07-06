# Python Switch-Like Control Structures
# Python does not have a native switch statement like other languages,
# but similar functionality can be achieved using if-elif-else, dictionary mapping, or match-case (Python 3.10+).

# 1. Using if-elif-else (classic way)
# Checks conditions one by one and executes the matching block.
day = 3

if day == 1:
    print("Monday")   # Executes if day is 1
elif day == 2:
    print("Tuesday")  # Executes if day is 2
elif day == 3:
    print("Wednesday") # Executes if day is 3
else:
    print("Invalid day")  # Executes if no conditions match

print("-----")

# 2. Using dictionary mapping (Pythonic way)
# Uses a dictionary to map keys to functions or values.
# Retrieves the function by key and calls it; uses a default function if key is not found.

def monday():
    return "Monday"

def tuesday():
    return "Tuesday"

def wednesday():
    return "Wednesday"

switch = {
    1: monday,     # Key 1 maps to monday() function
    2: tuesday,    # Key 2 maps to tuesday() function
    3: wednesday   # Key 3 maps to wednesday() function
}

day = 3
# Call the function from dictionary; if key not found, call lambda returning "Invalid day"
print(switch.get(day, lambda: "Invalid day")())

print("-----")

# 3. Using match-case (Python 3.10+)
# Pattern matching control structure similar to switch-case.
# Matches the value of 'day' and executes corresponding block.

day = 3

match day:
    case 1:
        print("Monday")      # Executes if day == 1
    case 2:
        print("Tuesday")     # Executes if day == 2
    case 3:
        print("Wednesday")   # Executes if day == 3
    case _:                  # Default case if no match
        print("Invalid day")
