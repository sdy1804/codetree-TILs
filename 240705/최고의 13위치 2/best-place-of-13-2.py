N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total_max1 = 0
for i in range(len(arr)-1):
    for j in range(len(arr[i])-2):
        now_max = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        if now_max >= total_max1:
            point_x, point_y = i, j
        total_max1 = max(total_max1, now_max)
# print(total_max1)

total_max2 = 0
for i in range(len(arr)-1):
    for j in range(len(arr[i])-2):
        if i == point_x and (j == point_y or j+1 == point_y or j+2 == point_y):
            continue
        now_max = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        total_max2 = max(total_max2, now_max)
# print(total_max2)
print(total_max1 + total_max2)