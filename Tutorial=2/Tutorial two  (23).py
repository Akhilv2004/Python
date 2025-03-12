numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
mode = max(frequency, key=frequency.get)
print("Mode:", mode)