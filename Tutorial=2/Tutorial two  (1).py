s = input("Enter a string: ")
print("".join(char for char in s if char.lower() not in "aeiou"))