def count_vowels(s):
    # Define a function to count vowels in string 's'
    
    vowels = "aeiouAEIOU"   # Define string of vowels (lower and uppercase)
    count = 0               # Initialize count to zero
    
    # Loop through each character in the string
    for char in s:
        # If character is in the vowels string
        if char in vowels:
            count += 1      # Increment the count by 1
    
    return count            # Return total vowel count

print(count_vowels("Interview"))  # Prints 4 (I, e, i, e)


#count vowels
def count_vowels(s):
    # Returns the number of vowels in string s
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # 3
