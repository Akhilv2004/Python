n = int(input("Enter a number: "))
sum_cubes = 0
for i in range(2, n + 1, 2):
    sum_cubes += i ** 3
print(f"Sum of cubes of even numbers: {sum_cubes}")
