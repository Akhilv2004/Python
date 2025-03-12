num = int(input("Enter a decimal number: "))
binary = ""
if num == 0:
    binary = "0"
while num > 0:
    binary = str(num % 2) + binary
    num //= 2
print("Binary number:", binary)