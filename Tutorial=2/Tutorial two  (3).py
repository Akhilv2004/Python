s = input("Enter a string: ")
n = len(s)
is_palindrome = True
for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        is_palindrome = False
        break
print("Palindrome" if is_palindrome else "Not a palindrome")