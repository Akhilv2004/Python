n = int(input("Enter the number of elements: "))
sum_even = 0
for _ in range(n):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        sum_even += num
print(f"Sum of even numbers: {sum_even}")
