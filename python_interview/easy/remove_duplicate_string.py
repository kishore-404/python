def remove_duplicates(s):
    # Remove duplicate characters from the string s
    # and return the string with characters in original order without repeats.
    
    result = ""  # Initialize empty string to store unique characters
    
    # Iterate over every character in s
    for char in s:
        # If character is NOT already in result, add it
        if char not in result:
            result += char
    
    # Return the string with duplicates removed
    return result

print(remove_duplicates("banana"))  # Output: 'ban'
print(remove_duplicates("apple"))   # Output: 'aple'