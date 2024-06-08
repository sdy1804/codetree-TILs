n, m = map(int, input().split())
arr_2d = [[0 for _ in range(m)] for _ in range(n)]
num = 1

for i in range(n):
    for j in range(m):
        arr_2d[i][j] = num
        num += 1

for column in arr_2d:
    for row in column:
        print(row, end=" ")
    print()