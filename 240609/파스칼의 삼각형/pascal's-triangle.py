n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr[i][0] = 1
for i, j in enumerate(range(n)):
    arr[i][j] = 1
if n >= 3:
    for i in range(2,n):
        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for a in arr:
    for b in a:
        if b != 0:
            print(b, end=" ")
        else:
            print(" ", end=" ")
    print()