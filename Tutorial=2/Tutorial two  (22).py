numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
numbers.sort()
mid = len(numbers) // 2
median = (numbers[mid] if len(numbers) % 2 != 0 
          else (numbers[mid - 1] + numbers[mid]) / 2)
print("Median:", median)