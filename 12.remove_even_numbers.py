numbers = []
n = int(input("Enter the number of elements:"))
for i in range(0, n):
    num = int(input("Enter the number:"))
    numbers.append(num)
print("Original list:", numbers)
updated_list = []
for i in range(0, n):
    if numbers[i] % 2 != 0:
        updated_list.append(numbers[i])
print("updated list:", updated_list)
