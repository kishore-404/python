def fibonacci(n):
    # Define function to print first n Fibonacci numbers
    
    a, b = 0, 1            # Initialize first two Fibonacci numbers
    
    # Loop n times
    for _ in range(n):
        print(a, end=" ")  # Print current number 'a' without newline
        a, b = b, a + b    # Update 'a' to 'b', and 'b' to sum of old a+b

fibonacci(5)  # Output: 0 1 1 2 3
