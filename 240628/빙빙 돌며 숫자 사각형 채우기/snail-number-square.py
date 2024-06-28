n, m = map(int, input().split())

ans = [[0] * m for _ in range(n)]
ans[0][0] = 1
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 동, 남, 서, 북
direct = 0

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

x, y = 0, 0
for i in range(2, n * m + 1):
    test_x, test_y = x + dx[direct], y + dy[direct]
    if not in_range(test_x, test_y) or ans[test_x][test_y] != 0:
        direct = (direct + 1) % 4
    bef = ans[x][y]
    # print(bef)
    x, y = x + dx[direct], y + dy[direct]
    # print(x, y)
    ans[x][y] = bef + 1
    # print(ans[x][y])

for elem in ans:
    for i in elem:
        print(i, end=" ")
    print()