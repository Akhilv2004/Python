password = input("Enter a password: ")

if (len(password) >= 6 and
    any('a' <= char <= 'z' for char in password) and
    any('A' <= char <= 'Z' for char in password) and
    any('0' <= char <= '9' for char in password) and
    any(char in "$#@" for char in password)):
    print("Valid password")
else:
    print("Invalid password")