nums = [int(input("Enter a number: ")) for _ in range(4)]
positive_sum = sum(num for num in nums if num > 0)
negative_sum = sum(num for num in nums if num < 0)
positive_avg = positive_sum / len([num for num in nums if num > 0]) if positive_sum != 0 else 0
negative_avg = negative_sum / len([num for num in nums if num < 0]) if negative_sum != 0 else 0
print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")
print(f"Average of positive numbers: {positive_avg}")
print(f"Average of negative numbers: {negative_avg}")
