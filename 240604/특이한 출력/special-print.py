n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if (i+j) % 4 == 0:
            print(f"{i, j}", end="\n")
        else:
            print(f"{i, j}", end=" ")