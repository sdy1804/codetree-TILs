n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

m = n - 1
for i in range(n):
    for j in range(m):
        print("*", end=" ")
    m -= 1
    print()