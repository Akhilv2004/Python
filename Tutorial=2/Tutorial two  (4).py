s = input("Enter a string: ")
print(s.replace(" ", "*") if " " in s else f"${s}$")