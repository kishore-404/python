# -----------------------------
# 💡 Definitions
# -----------------------------
# ➤ Operator: A symbol that performs an operation on values (operands).
# ➤ Operand: The values or variables on which the operator acts.
# Example: In 3 + 5, "+" is the operator, and 3 and 5 are operands.

# -----------------------------
# 1. Arithmetic Operators
# -----------------------------
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333... - Quotient
print("Floor Division:", a // b) # 3 - Quotient
print("Modulus:", a % b)         # 1 - remainder
print("Exponent:", a ** b)       # 1000

# -----------------------------
# 2. Comparison (Relational) Operators
# Returns True or False
# -----------------------------
a = 10
b = 3
print("\nComparison Operators:")
print("a == b:", a == b)  # False
print("a != b:", a != b)  # True
print("a > b:", a > b)    # True
print("a < b:", a < b)    # False
print("a >= b:", a >= b)  # True
print("a <= b:", a <= b)  # False

# Usage in if-else
if a > b:
    print("a is greater than b")
else:
    print("b is greater or equal to a")

# -----------------------------
# 3. Logical Operators
# Used to combine conditional statements
# -----------------------------
x = 5
print("\nLogical Operators:")
print("x > 0 and x < 10:", x > 0 and x < 10)  # True
print("x < 0 or x > 2:", x < 0 or x > 2)      # True
print("not(x > 0):", not(x > 0))              # False

# Logical operator in if
if x > 0 and x < 10:
    print("x is a positive single-digit number")

# -----------------------------
# 4. Assignment Operators
# Used to assign values to variables
# -----------------------------
print("\nAssignment Operators:")
c = 5     # assign
c += 3    # c = c + 3 → 8
print("c after += 3:", c)
c *= 2    # c = c * 2 → 16
print("c after *= 2:", c)

# -----------------------------
# 5. Bitwise Operators
# Work on binary level
# -----------------------------
a = 10  #10 in binary = 1010
b = 3   #3 in binary = 0011
print("\nBitwise Operators:")
print("a & b (AND):", a & b)   # 10 & 3 = 2  
print("a | b (OR):", a | b)    # 10 | 3 = 11
print("a ^ b (XOR):", a ^ b)   # 10 ^ 3 = 9
print("~a (NOT):", ~a)         # ~10 = -11          ~a == -(a + 1) - shortcut
print("a << 1:", a << 1)       # Left shift = 20    Left shift by n	 , Multiply by 2ⁿ
print("a >> 1:", a >> 1)       # Right shift = 5

# -----------------------------
# 6. Identity Operators
# Used to compare memory locations
# -----------------------------
print("\nIdentity Operators:")
x = [1, 2]
y = [1, 2]
z = x

print("x is z:", x is z)       # True (same object)
print("x is y:", x is y)       # False (same value, different objects)
print("x is not y:", x is not y)  # True

# -----------------------------
# 7. Membership Operators
# Used to check if a value exists in a sequence
# -----------------------------
print("\nMembership Operators:")
nums = [1, 2, 3, 4, 5]
print("3 in nums:", 3 in nums)        # True
print("6 not in nums:", 6 not in nums)  # True

# -----------------------------
# Summary:
# -----------------------------
# 1. Arithmetic: + - * / // % **
# 2. Comparison: == != > < >= <=
# 3. Logical: and or not
# 4. Assignment: = += -= *= /= //= %= **=
# 5. Bitwise: & | ^ ~ << >>
# 6. Identity: is, is not
# 7. Membership: in, not in


# ~10 = 11110101
# To find the decimal value of a negative two’s complement number:
# Invert bits again
# Add 1
# Convert to decimal and add a negative sign

# The left shift operator (<<) shifts the bits of a binary number to the left by a specified number of positions.