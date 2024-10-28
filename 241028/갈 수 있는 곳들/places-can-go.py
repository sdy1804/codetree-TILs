from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start_points = [list(map(int, input().split())) for _ in range(k)]

# 각 시작지점에서 BFS 탐색
# ans에 수를 입력
# ans를 탐색하여 0이 아닌 수를 카운트

visited = [[0 for _ in range(n)] for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]
q = deque()
order = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if visited[x][y] == 1 or grid[x][y] == 1:
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
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            next_x, next_y = x + dx, y + dy
            if can_go(next_x, next_y):
                push(next_x, next_y)

for i in range(len(start_points)):
    push(start_points[i][0]-1, start_points[i][1]-1)
    BFS()
# print(ans)

count_ans = 0
for r in range(n):
    for c in range(n):
        if ans[r][c] != 0:
            count_ans += 1
print(count_ans)