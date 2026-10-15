n = int(input("Enter the number of names: "))
names = []
for i in range(n):
    names.append(input("Enter first name: "))
count = 0
for name in names:
    for ch in name:
        if ch == 'a':
            count += 1
print("Names:", names)
print("Occurrences of 'a' in the list:", count)
