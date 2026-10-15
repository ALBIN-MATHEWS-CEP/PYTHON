numbers = []
n = int(input("Enter the number of elements in the list:"))
for i in range(0, n):
    element = int(input("Enter an element:"))
    numbers.append(element)
print("Positive numbers are:")
for i in range(0, n):
    if (numbers[i] > 0):
        print(numbers[i])
