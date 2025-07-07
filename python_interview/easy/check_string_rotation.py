def are_rotations(s1, s2):
    # Two strings are rotations if s2 is in s1+s1
    return len(s1) == len(s2) and s2 in s1 + s1

print(are_rotations("abcde", "cdeab"))  # True
print(are_rotations("abc", "acb"))      # False
