def is_prime(n):
    # Check if the number is less than 2
    # Numbers less than 2 are NOT prime by definition
    if n < 2:
        return False
    
    # Loop from 2 up to the square root of n (inclusive)
    # We only need to check divisors up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by any number in this range,
        # it means n is NOT prime
        if n % i == 0:
            return False  # Exit early since n is not prime
    
    # If no divisors found, n is prime
    return True

# Take input from the user as an integer
num = int(input("Enter a number to check if it is prime: "))

# Call the function and store the result
result = is_prime(num)

# Print whether the number is prime or not
if result:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is NOT a prime number.")
