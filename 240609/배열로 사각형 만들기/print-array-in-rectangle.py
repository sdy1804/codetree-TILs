n = 5
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr[0][i] = 1
    arr[i][0] = 1

for i in range(1,n):
    for j in range(1,n):
        arr[i][j] = arr[i][j-1] + arr[i-1][j]

for column in arr:
    for row in column:
        print(row, end=" ")
    print()