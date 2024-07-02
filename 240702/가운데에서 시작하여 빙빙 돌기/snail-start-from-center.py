n = int(input())

sqr = [[0] * n for _ in range(n)]
x, y = n // 2, n // 2
sqr[x][y] = 1

dx, dy = [0, -1, 0, 1], [1, 0, -1, 0] # 동,북,서,남
direct = 0
if n > 1:
    x, y = x + dx[direct], y + dy[direct]
    sqr[x][y] = 2
# print(sqr)

# 방향을 바꾸는 조건 설정
# 오른쪽으로 갈 때 : 위가 비어있으면 위로 올라감 / 위가 차있으면 위가 빌 때까지 오른쪽으로 감
# 위로 갈 때 : 왼쪽이 비어있으면 왼쪽으로 감 / 왼쪽이 차있으면 왼쪽이 빌 때까지 위로 감
# 왼쪽으로 갈 때 : 아래가 비어있으면 아래로 감 / 아래가 차있으면 아래가 빌 때까지 왼쪽으로 감
# 아래로 갈 때 : 오른쪽이 비어있으면 오른쪽으로 감 / 오른쪽이 차있으면 오른쪽이 빌 때까지 아래로 감
# 모든 방향은 out of range면 다음 방향으로 꺾는다

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


for i in range(3, n*n + 1):
    next_direct = (direct + 1) % 4
    bef_val = sqr[x][y]
    nx, ny = x + dx[direct], y + dy[direct]
    if not in_range(nx, ny) or sqr[x + dx[next_direct]][y + dy[next_direct]] == 0:
        direct = next_direct
        x, y = x + dx[direct], y + dy[direct]
        sqr[x][y] = bef_val + 1
    else:
        x, y = x + dx[direct], y + dy[direct]
        sqr[x][y] = bef_val + 1

for elem in sqr:
    for i in elem:
        print(i, end=" ")
    print()