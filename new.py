# 1. 
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# 2. 
for i in range(1, 4):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 3. 
rows = 5
cols = 6

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 4. 
for i in range(1, 4):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
for i in range(65,130):
    print(f"{i} {chr(i)}");