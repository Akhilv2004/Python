binary = input("Enter a binary number: ")
decimal = 0
for i in range(len(binary)):
    decimal += int(binary[-(i + 1)]) * (2 ** i)
print("Decimal number:", decimal)