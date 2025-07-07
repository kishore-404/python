def char_frequency(s):
    # Count the frequency of each character in the string s
    # and return a dictionary with char as key and count as value.
    
    freq = {}  # Create an empty dictionary to store frequencies
    
    # Iterate over each character in s
    for char in s:
        # Use dict.get() to get current count of char or 0 if not found
        # Then add 1 to the count and update dictionary
        freq[char] = freq.get(char, 0) + 1
    
    # Return the dictionary with frequencies
    return freq

print(char_frequency("banana"))  # Output: {'b': 1, 'a': 3, 'n': 2}
