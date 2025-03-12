string = input("Enter a string: ")
words_to_remove = input("Enter words to remove (separated by spaces): ").split()
result = " ".join(word for word in string.split() if word not in words_to_remove)
print("Result:", result)