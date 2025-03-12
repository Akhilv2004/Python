import math

x = float(input("Enter the value of x in degrees: "))
n = int(input("Enter the number of terms: "))

x_rad = math.radians(x)
sin_x = 0

for i in range(n):
    term = ((-1) ** i) * (x_rad ** (2 * i + 1)) / math.factorial(2 * i + 1)
    sin_x += term

print(f"sin({x}) ≈ {sin_x}")