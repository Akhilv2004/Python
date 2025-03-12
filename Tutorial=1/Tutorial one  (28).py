lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
total = 0

for num in range(lower, upper + 1):
    if num % 2 != 0:
        total += num

print("Sum of odd numbers:", total)