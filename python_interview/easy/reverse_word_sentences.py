def reverse_words(sentence):
    # Reverse the order of words in a sentence.
    # For example, "hello world" becomes "world hello"
    
    # Split the sentence into words (list of strings)
    words = sentence.split()
    
    # Reverse the list of words using slicing [::-1]
    reversed_words = words[::-1]
    
    # Join the reversed list of words back into a single string separated by spaces
    return " ".join(reversed_words)

print(reverse_words("hello world from python"))  # Output: "python from world hello"