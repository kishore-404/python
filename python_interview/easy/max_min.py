def find_min(lst):
    # Function to find the smallest number in a list
    
    min_num = lst[0]  # Initialize min_num with the first element of the list
    
    for num in lst:   # Loop through each number in the list
        if num < min_num:  # If current number is smaller than min_num
            min_num = num  # Update min_num to this smaller number
            
    return min_num  # After checking all numbers, return the smallest one

# Test the function with a sample list
print(find_min([4, 2, 9, 1, 5]))  # Output will be 1

def find_max(lst):
    # Function to find the smallest number in a list
    
    min_num = lst[0]  # Initialize min_num with the first element of the list
    
    for num in lst:   # Loop through each number in the list
        if num > min_num:  # If current number is smaller than min_num
            min_num = num  # Update min_num to this smaller number
            
    return min_num  # After checking all numbers, return the smallest one

# Test the function with a sample list
print(find_max((4, 2, 9, 1, 5)))  # Output will be 1
