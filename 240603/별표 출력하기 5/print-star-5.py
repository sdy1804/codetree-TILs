n = int(input())
m = n

for i in range(n):
    for k in range(m):
        for j in range(m):
            print("*", end="")
        print(" ", end="")
    m -= 1
    print()