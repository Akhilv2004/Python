def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = list(map(int, input("Enter positive integers: ").split()))
primes = [num for num in numbers if is_prime(num)]
composites = [num for num in numbers if num > 1 and num not in primes]
print("Prime numbers:", primes)
print("Composite numbers:", composites)
