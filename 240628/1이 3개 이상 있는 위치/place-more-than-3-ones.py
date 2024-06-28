n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

total_cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        cnt = 0
        for dxs, dys in zip(dx, dy):
            nx, ny = i + dxs, j + dys
            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            total_cnt += 1
print(total_cnt)