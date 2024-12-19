def capitalize_words(input_string):
    return ' '.join(word.capitalize() for word in input_string.split())

# Example Usage
print(capitalize_words("hi"))                  # Output: "Hi"
print(capitalize_words("i love programming")) # Output: "I Love Programming"
