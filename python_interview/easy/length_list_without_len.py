def list_length(lst):
    # Define function to find length of list without using len()
    
    count = 0              # Initialize counter to zero
    
    # Loop over each item in the list
    for _ in lst:
        count += 1         # Increment count for each item
    
    return count           # Return the final count

print(list_length([1, 2, 3, 4, 5]))  # Prints 5


