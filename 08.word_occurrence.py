str = input("Enter the string:")
search = input("Enter the word to be searched:")
x = str.split(" ")
count = 0
for i in x:
    if (i == search):
        count = count + 1
print("Total occurrences of the word is:", count)
