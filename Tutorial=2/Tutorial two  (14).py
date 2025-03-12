def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(f"{n}C{r} =", nCr(n, r))