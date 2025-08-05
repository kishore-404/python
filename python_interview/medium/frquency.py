# Program to count the frequency of each letter in a user-provided input string

# Take input from the user
input_string = input("Enter a string: ")

# Convert the input to lowercase to count letters in a case-insensitive manner
input_string = input_string.lower()

# Create an empty dictionary to store the frequency of each character
frequency = {}

# Loop through each character in the string
for char in input_string:
    # Check if the character is a letter (ignores numbers, spaces, and symbols)
    if char.isalpha():
        # If the letter is already in the dictionary, increase its count
        if char in frequency:
            frequency[char] += 1
        # If it's not yet in the dictionary, add it with a count of 1
        else:
            frequency[char] = 1

# Display the results
print("\nLetter Frequencies:")
for letter, count in sorted(frequency.items()):
    print(f"{letter}: {count}")
