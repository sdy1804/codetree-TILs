n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
start_num = 1

for i in range(n):
    start_num = 1 + i
    for j in range(n):
        arr[i][j] = start_num
        start_num += n

for column in arr:
    for row in column:
        print(row, end=" ")
    print()