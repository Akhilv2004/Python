num = int(input("Enter a number: "))
power = len(str(num))
total = sum(int(digit) ** power for digit in str(num))
print(f"{num} is an Armstrong number" if num == total else f"{num} is not an Armstrong number")