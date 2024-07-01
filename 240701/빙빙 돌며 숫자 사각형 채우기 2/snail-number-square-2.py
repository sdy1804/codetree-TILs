n, m = map(int, input().split())

sqr = [[0] * m for _ in range(n)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # 남, 동, 북, 서
x, y = 0, 0
sqr[x][y] = 1
direct = 0 # 남쪽

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

for i in range(2, n*m + 1):
    bef_val = sqr[x][y]
    nx, ny = x + dx[direct], y + dy[direct]
    if not in_range(nx, ny) or sqr[nx][ny] != 0:
        direct = (direct + 1) % 4
    x, y = x + dx[direct], y + dy[direct]
    sqr[x][y] = bef_val + 1

for elem in sqr:
    for i in elem:
        print(i, end=" ")
    print()