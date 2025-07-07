def square_star_pattern(n):
    # Print a square pattern of stars (n rows x n columns)
    print("Square pattern with stars:")
    for i in range(n):              # Loop through each row
        print('*' * n)              # Print n stars per row
    print()  # Blank line

# Output:
# Square pattern with stars:
# ****
# ****
# ****
# ****


def square_number_pattern(n):
    # Print a square pattern with numbers 1 to n in each row
    print("Square pattern with numbers:")
    for i in range(n):              # Loop through rows
        for j in range(1, n + 1):   # Print numbers 1 to n
            print(j, end='')        # Print on same line
        print()                     # New line after each row
    print()  # Blank line

# Output:
# Square pattern with numbers:
# 1234
# 1234
# 1234
# 1234


def square_alphabet_pattern(n):
    # Print a square pattern with alphabets A to A+n-1 in each row
    print("Square pattern with alphabets:")
    for i in range(n):              # Loop through rows
        for j in range(n):          # Loop for columns
            print(chr(65 + j), end='')  # chr(65) is 'A'
        print()                     # New line after each row
    print()  # Blank line

# Output:
# Square pattern with alphabets:
# ABCD
# ABCD
# ABCD
# ABCD


# 🔹 Driver Code
n = 4
square_star_pattern(n)
square_number_pattern(n)
square_alphabet_pattern(n)
