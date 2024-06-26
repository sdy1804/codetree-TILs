n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

set_point = 210
ans = [[0] * set_point for _ in range(set_point)]

OFFSET = 0
for i in range(n):
    for j in range(len(arr[i])):
        if arr[i][j] < OFFSET:
            OFFSET = arr[i][j]
for i in range(n):
    for k in range(len(arr[i])):
        arr[i][k] += abs(OFFSET)

for i in range(n):
    if i % 2 == 0: # 빨간색 칠하기
        for j in range(arr[i][0], arr[i][2]):
            for k in range(arr[i][1], arr[i][3]):
                ans[j][k] = 1
    else:
        for j in range(arr[i][0], arr[i][2]):
            for k in range(arr[i][1], arr[i][3]):
                ans[j][k] = 2

count = 0
for i in range(len(ans)):
    count += ans[i].count(2)
print(count)