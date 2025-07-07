def is_armstrong(num):
    # Convert number to string to easily iterate over each digit
    num_str = str(num)
    
    # Get the number of digits (length of the string)
    num_digits = len(num_str)
    
    # Initialize sum to store sum of each digit raised to the power of num_digits
    total = 0
    
    # Loop through each digit in the string
    for digit in num_str:
        # Convert the digit back to int and raise it to the power of num_digits
        total += int(digit) ** num_digits
    
    # Check if the sum equals the original number
    return total == num

# Test cases
print(is_armstrong(153))  # True (1^3 + 5^3 + 3^3 = 153)
print(is_armstrong(9474)) # True (4-digit Armstrong number)
print(is_armstrong(123))  # False (not Armstrong)
print(is_armstrong(370))  # True (3-digit Armstrong number)
