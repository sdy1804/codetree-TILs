n = int(input())

for i in range(1, n+1):
    for j in range(n*i, i-1, -i):
        print(j, end=" ")
    print()