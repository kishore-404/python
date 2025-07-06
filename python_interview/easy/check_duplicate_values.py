def has_duplicates(lst):
    # Returns True if list has any duplicates
    return len(lst) != len(set(lst))

print(has_duplicates([1, 2, 3, 2]))  # True
print(has_duplicates([1, 2, 3]))     # False


