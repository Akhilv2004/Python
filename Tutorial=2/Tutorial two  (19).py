names = []
n = int(input("Enter the number of names: "))
for _ in range(n):
    names.append(input("Enter name: "))
names.sort()
print("Sorted names:", names)