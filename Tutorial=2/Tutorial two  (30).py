numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
unique_numbers = [num for num in numbers if numbers.count(num) == 1]
print("List after removing all duplicates:", unique_numbers)