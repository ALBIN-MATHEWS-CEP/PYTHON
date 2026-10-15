n1 = int(input("Enter the number of elements in first list: "))
list1 = []
for i in range(n1):
    list1.append(int(input("Enter the number: ")))
n2 = int(input("Enter the number of elements in second list: "))
list2 = []
for i in range(n2):
    list2.append(int(input("Enter the number: ")))

print("List 1:", list1)
print("List 2:", list2)

# a) same length
if len(list1) == len(list2):
    print("The lists are of the same length")
else:
    print("The lists are not of the same length")

# b) same sum
if sum(list1) == sum(list2):
    print("The lists sum to the same value")
else:
    print("The lists do not sum to the same value")

# c) common values
common = []
for x in list1:
    if x in list2 and x not in common:
        common.append(x)
if common:
    print("Values occurring in both lists:", common)
else:
    print("No value occurs in both lists")
