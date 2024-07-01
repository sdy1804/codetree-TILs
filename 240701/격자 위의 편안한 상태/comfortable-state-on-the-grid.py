N, M = map(int, input().split())
sqr = [[0] * N for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(M)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

for i in range(M):
    x, y = arr[i][0] - 1, arr[i][1] - 1
    # print('x, y',x, y)
    sqr[x][y] = 1
    cnt = 0
    for j in range(len(dx)):
        nx, ny = x + dx[j], y + dy[j] # j=0 -> 북, j=1 -> 동, j=2 -> 남, j=3 -> 서
        # print('nx, ny', nx, ny)
        if in_range(nx, ny):
            # print('sqr[nx][ny]',sqr[nx][ny])
            if sqr[nx][ny] == 1:
                cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)