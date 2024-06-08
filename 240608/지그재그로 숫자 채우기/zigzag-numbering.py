n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
# print(arr)
start_num = 0

for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            arr[j][i] = start_num
            start_num += 1
    else:
        for j in range(n-1, -1, -1):
            arr[j][i] = start_num
            start_num += 1

for column in arr:
    for row in column:
        print(row, end=" ")
    print()