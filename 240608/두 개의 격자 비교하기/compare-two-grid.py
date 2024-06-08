n, m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

new_arr = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            new_arr[i][j] = 0
        else:
            new_arr[i][j] = 1

for column in new_arr:
    for row in column:
        print(row, end=" ")
    print()