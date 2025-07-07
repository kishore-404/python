def first_non_repeating_char(s):
    # Iterate over characters and check counts
    for char in s:
        if s.count(char) == 1:
            return char
    return None

print(first_non_repeating_char("swiss"))  # w
print(first_non_repeating_char("aabbcc")) # None
