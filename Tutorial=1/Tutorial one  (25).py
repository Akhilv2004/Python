x = int(input("Enter base (X): "))
y = int(input("Enter exponent (Y): "))
result = 1
for _ in range(y):
    result *= x
print(result)