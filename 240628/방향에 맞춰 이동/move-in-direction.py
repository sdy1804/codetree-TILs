N = int(input())
arr = [list(input().split()) for _ in range(N)]
for i in range(N):
    arr[i][1] = int(arr[i][1])

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 동, 남, 서, 북
nx, ny = 0, 0

for i in range(len(arr)):
    if arr[i][0] == 'E':
        idx = 0
        for j in range(arr[i][1]):
            nx, ny = nx + dx[idx], ny + dy[idx]
    elif arr[i][0] == 'S':
        idx = 1
        for j in range(arr[i][1]):
            nx, ny = nx + dx[idx], ny + dy[idx]
    elif arr[i][0] == 'W':
        idx = 2
        for j in range(arr[i][1]):
            nx, ny = nx + dx[idx], ny + dy[idx]
    else:
        idx = 3
        for j in range(arr[i][1]):
            nx, ny = nx + dx[idx], ny + dy[idx]
print(nx, ny)