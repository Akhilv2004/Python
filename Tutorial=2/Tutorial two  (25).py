strings into different lists
data = input("Enter data separated by spaces: ").split()
integers, floats, strings = [], [], []
for item in data:
    try:
        if '.' in item:
            floats.append(float(item))
        else:
            integers.append(int(item))
    except ValueError:
        strings.append(item)
print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)