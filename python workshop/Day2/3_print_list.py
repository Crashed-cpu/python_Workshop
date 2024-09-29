# python program to create a list of user defined elements and print

i = 0
LIST = []
j = int(input("Enter no of elements in the list: "))

while i < j:
    i += 1
    x = int(input("Enter a number: "))
    LIST.append(x)

print(LIST)