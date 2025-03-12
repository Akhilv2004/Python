num = int(input("Enter a number: "))
factor = 2
while num > 1:
    if num % factor == 0:
        print(factor, end=' ')
        num //= factor
    else:
        factor += 1