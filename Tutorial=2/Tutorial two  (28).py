set1 = set(map(int, input("Enter elements of set 1: ").split()))
set2 = set(map(int, input("Enter elements of set 2: ").split()))
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)