from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
q = deque()
order = 1

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    return True

def push(x, y):
    global order

    ans[x][y] = order
    order += 1
    visited[x][y] = 1
    q.append((x, y))

def BFS():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        x, y = q.popleft() # 현재 좌표를 가져옴
        for dx, dy in zip(dxs, dys): # 현재 좌표 근처를 탐색
            next_x, next_y = x + dx, y + dy
            if can_go(next_x, next_y):
                push(next_x, next_y)

push(0, 0)
BFS()
# print(ans)
if ans[n-1][m-1]:
    print(1)
else:
    print(0)