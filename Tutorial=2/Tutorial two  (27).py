def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sort_list(numbers)
print("Sorted list:", numbers)