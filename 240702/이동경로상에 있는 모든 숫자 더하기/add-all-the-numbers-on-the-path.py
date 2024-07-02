N, T = map(int, input().split())
command = input()
sqr = [list(map(int, input().split())) for _ in range(N)]

x, y = N//2 , N//2
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
direct = 0 # 북

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

sum = sqr[x][y]
for i in range(T):
    if command[i] == 'L':
        direct = (direct - 1 + 4) % 4
    elif command[i] == 'R':
        direct = (direct + 1) % 4
    else:
        nx, ny = x + dx[direct], y + dy[direct]
        if not in_range(nx, ny):
            sum += 0
        else:
            x, y = x + dx[direct], y + dy[direct]
            sum += sqr[x][y]
print(sum)