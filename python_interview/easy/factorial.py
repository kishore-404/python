def factorial(n):
    # Define a function to calculate factorial of number 'n'
    
    result = 1            # Initialize result as 1 (factorial identity)
    
    # Loop i from 1 up to and including n
    for i in range(1, n+1):
        result *= i       # Multiply result by i on each iteration
    
    return result         # Return the computed factorial value

print(factorial(5))      # Prints 120 (5! = 1*2*3*4*5)
