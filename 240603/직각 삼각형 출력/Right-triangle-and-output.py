n = int(input())
m = 1
for i in range(n):
    for j in range(m):
        print("*", end="")
    m += 2
    print()