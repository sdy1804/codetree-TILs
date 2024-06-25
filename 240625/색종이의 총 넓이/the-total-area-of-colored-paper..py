N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

OFFSET = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < OFFSET:
            OFFSET = arr[i][j]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] += abs(OFFSET)
# print(arr)

ans = [[0] * 1000 for _ in range(1000)]
for i in range(N):
    for j in range(arr[i][0], arr[i][0] + 8):
        for k in range(arr[i][1], arr[i][1] + 8):
            ans[j][k] = 1
# print(ans)
count = 0
for i in range(len(ans)):
    count += ans[i].count(1)
print(count)