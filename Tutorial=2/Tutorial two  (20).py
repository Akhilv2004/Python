n = int(input("Enter the number of numbers: "))
total = 0
for _ in range(n):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        total += num
print("Sum of even numbers:", total)