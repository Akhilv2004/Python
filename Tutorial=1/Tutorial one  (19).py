n = int(input("Enter the number of elements: "))
even = odd = 0
for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)