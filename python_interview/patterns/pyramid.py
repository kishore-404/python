def pyramid_star_pattern(n):
    # Print a centered pyramid of stars with n rows
    print("Pyramid pattern with stars:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)           # Padding spaces for centering
        stars = '*' * (2 * i - 1)        # Odd number of stars: 1, 3, 5...
        print(spaces + stars)
    print()

# Output:
# Pyramid pattern with stars:
#    *
#   ***
#  *****
# *******


def pyramid_number_pattern(n):
    # Print a centered pyramid with increasing numbers
    print("Pyramid pattern with numbers:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)           # Padding for centering
        numbers = ''.join(str(j) for j in range(1, 2 * i))  # 1 to 2*i - 1
        print(spaces + numbers)
    print()

# Output:
# Pyramid pattern with numbers:
#    1
#   123
#  12345
# 1234567


def pyramid_alphabet_pattern(n):
    # Print a centered pyramid with alphabets starting from 'A'
    print("Pyramid pattern with alphabets:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        chars = ''.join(chr(65 + j) for j in range(2 * i - 1))  # A, B, C...
        print(spaces + chars)
    print()

# Output:
# Pyramid pattern with alphabets:
#    A
#   ABC
#  ABCDE
# ABCDEFG


# 🔹 Driver Code
n = 4
pyramid_star_pattern(n)
pyramid_number_pattern(n)
pyramid_alphabet_pattern(n)
