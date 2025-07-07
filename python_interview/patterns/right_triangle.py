def right_angle_star(n):
    # Print a right-angled triangle of stars with 'n' rows
    print("Right-angled triangle with stars:")
    for i in range(1, n + 1):  # Loop through rows 1 to n
        print('*' * i)         # Print i stars in each row
    print()  # Blank line for separation

# output

# Right-angled triangle with stars:
# *
# **
# ***
# ****
# *****   

def right_angle_numbers(n):
    # Print a right-angled triangle with numbers incrementing per row
    print("Right-angled triangle with numbers:")
    for i in range(1, n + 1):       # Loop through rows 1 to n
        for j in range(1, i + 1):   # Print numbers from 1 to i in each row
            print(j, end='')        # Print numbers on the same line
        print()                     # Move to the next line after each row
    print()  # Blank line for separation

# output   
# Right-angled triangle with numbers:
# 1
# 12
# 123
# 1234
# 12345

def right_angle_alphabets(n):
    # Print a right-angled triangle with alphabets starting from 'A'
    print("Right-angled triangle with alphabets:")
    for i in range(1, n + 1):       # Loop through rows 1 to n
        for j in range(i):           # Print characters from 'A' up to 'A'+i-1
            print(chr(65 + j), end='')  # Convert ASCII code to char
        print()                     # Move to next line
    print()  # Blank line for separation


# Right-angled triangle with alphabets:
# A
# AB
# ABC
# ABCD
# ABCDE

# Driver code: call all functions with n = 5
n = 5

right_angle_star(n)
right_angle_numbers(n)
right_angle_alphabets(n)




