n, m = map(int, input().split())

sqr = [[0]*m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
direct = 0 # 동쪽
sqr[0][0] = chr(ord('A'))
# print(ord('A'))
# print(chr(65))

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

for i in range(2, n*m + 1):
    bef_val = ord(sqr[x][y])
    # print(bef_val)
    nx, ny = x + dx[direct], y + dy[direct]
    if not in_range(nx, ny) or sqr[nx][ny] != 0:
        direct = (direct + 1) % 4
    x, y = x + dx[direct], y + dy[direct]
    if chr(bef_val) == 'Z':
        sqr[x][y] = 'A'
    else:
        sqr[x][y] = chr(bef_val + 1)

for elem in sqr:
    for i in elem:
        print(i, end=" ")
    print()