n = int(input("enter number of rows: "))
num = 1
for row in range(0, n):
    for col in range(0, row + 1):
        print(num, end=" ")
        num += 1
    print()