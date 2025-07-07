def inverted_star_pyramid(n):
    # Print an inverted centered pyramid of stars
    print("Inverted pyramid with stars:")
    for i in range(n, 0, -1):            # Start from n down to 1
        spaces = ' ' * (n - i)           # Left padding to center
        stars = '*' * (2 * i - 1)        # Decreasing odd number of stars
        print(spaces + stars)
    print()

# Output:
# Inverted pyramid with stars:
# *******
#  *****
#   ***
#    *


def inverted_number_pyramid(n):
    # Print an inverted pyramid of numbers starting from 1
    print("Inverted pyramid with numbers:")
    for i in range(n, 0, -1):
        spaces = ' ' * (n - i)
        numbers = ''.join(str(j) for j in range(1, 2 * i))  # Numbers from 1 to 2i-1
        print(spaces + numbers)
    print()

# Output:
# Inverted pyramid with numbers:
# 1234567
#  12345
#   123
#    1


def inverted_alphabet_pyramid(n):
    # Print an inverted pyramid of alphabets starting from 'A'
    print("Inverted pyramid with alphabets:")
    for i in range(n, 0, -1):
        spaces = ' ' * (n - i)
        alphabets = ''.join(chr(65 + j) for j in range(2 * i - 1))  # A to ...
        print(spaces + alphabets)
    print()

# Output:
# Inverted pyramid with alphabets:
# ABCDEFG
#  ABCDE
#   ABC
#    A


# 🔹 Driver Code
n = 4
inverted_star_pyramid(n)
inverted_number_pyramid(n)
inverted_alphabet_pyramid(n)
