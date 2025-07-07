def are_anagrams(s1, s2):
    # Function to check if two strings s1 and s2 are anagrams
    # Anagrams mean both strings have the same characters in any order
    
    # sorted() function sorts the characters of the string alphabetically
    # For example, sorted("listen") -> ['e', 'i', 'l', 'n', 's', 't']
    # Similarly, sorted("silent") -> ['e', 'i', 'l', 'n', 's', 't']
    
    # If the sorted lists of characters are equal,
    # then s1 and s2 are anagrams, so return True
    # Otherwise, return False
    return sorted(s1) == sorted(s2)

# Test the function with two example inputs

print(are_anagrams("listen", "silent"))  
# Both strings have the same letters in different order
# sorted("listen") == sorted("silent") => True

print(are_anagrams("hello", "world"))    
# These strings do not have the same letters
# sorted("hello") != sorted("world") => False
