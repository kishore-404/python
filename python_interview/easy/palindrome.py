def is_palindrome(s):
    # Define function to check if 's' is a palindrome
    
    # Compare string with its reverse (using slicing s[::-1])
    return s == s[::-1]

print(is_palindrome("madam"))  # True (reads same backward)
print(is_palindrome("hello"))  # False (different backward)


#without slice operator

def is_palindromes(s):
    # Define function to check if 's' is a palindrome
    
    length = len(s)             # Get the length of the string
    
    # Loop from start to the middle of the string
    for i in range(length // 2):
        # Compare the character at position i with the character
        # at the "mirrored" position from the end
        if s[i] != s[length - 1 - i]:
            return False        # If mismatch found, it's NOT a palindrome
    
    # If no mismatches found, the string is a palindrome
    return True

print(is_palindromes("madam"))  # True (reads same backward)
print(is_palindromes("hello"))  # False (different backward)
