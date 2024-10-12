from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]
order = 1
q = deque()

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    return True

def push(x, y, s):
    global order

    ans[x][y] = order
    order += 1
    visited[x][y] = 1
    step[x][y] = s
    q.append((x, y))

def BFS():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy
            if can_go(next_x, next_y):
                push(next_x, next_y, step[x][y]+1)

push(0, 0, 0)
BFS()
# print(step)
if step[n-1][m-1]:
    print(step[n-1][m-1])
else:
    print(-1)