def are_rotations(s1, s2):
    # Check if two strings s1 and s2 are rotations of each other.
    # For example, "abcde" and "cdeab" are rotations because
    # "cdeab" appears inside "abcdeabcde" (s1+s1).
    
    # First, check if both strings are the same length,
    # because rotations must be equal length.
    if len(s1) != len(s2):
        return False
    
    # Check if s2 is a substring of s1 concatenated with itself.
    # If yes, s2 is a rotation of s1.
    return s2 in s1 + s1

print(are_rotations("abcde", "cdeab"))  # True
print(are_rotations("abc", "acb"))      # False