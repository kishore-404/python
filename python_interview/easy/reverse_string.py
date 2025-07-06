def reverse_string(s):
    # Define a function that takes a string 's'
    
    # Return the reversed string using slicing syntax [start:stop:step]
    # step = -1 means start from the end and move backwards
    return s[::-1]

print(reverse_string("hello"))  # Prints "olleh"

# without slice opertor

def reverse_string(s):
    # Define a function that takes a string 's'
    
    reversed_str = ""        # Initialize an empty string to hold the reversed result
    
    # Loop through each character in the input string starting from the end
    # Using a range starting from last index (len(s)-1) down to 0 (inclusive)
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]  # Append the character at position i to reversed_str
    
    return reversed_str       # Return the reversed string

print(reverse_string("hello"))  # Prints "olleh"