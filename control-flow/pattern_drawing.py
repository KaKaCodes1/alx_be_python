patternSize = int(input("Enter the size of the pattern: "))
row = 1

while row <= patternSize:
    for col in range(patternSize):
        print("*", end="")
    print()
    row += 1