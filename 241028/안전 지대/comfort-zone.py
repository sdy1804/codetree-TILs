N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 그리드를 탐색하여 최대값을 찾음 -> K의 최대값으로 설정
# 해당 최대값까지 바꿔가며 DFS 탐색
# 탐색하며 구역이 시작될 때, 1로 시작하여 최대 1의 값을 카운트
# K를 바꿔가며 탐색했을 때, 구역이 현재보다 크면 K값과 구역을 갱신. 그 외에는 갱신 X

visited = [[0 for _ in range(M)] for _ in range(N)]
ans = [[0 for _ in range(M)] for _ in range(N)]
order = 1

# 그리드 내 최대 K값 탐색
def find_max_K():
    max_K = 0
    for i in range(N):
        for j in range(M):
            if max_K < grid[i][j]:
                max_K = grid[i][j]
    return max_K

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

# K값을 기준으로 이동
def can_go(x, y, K):
    if not in_range(x, y):
        return False
    
    if visited[x][y] == 1 or grid[x][y] <= K:
        return False
    return True

def DFS(x, y, K):
    global order
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        next_x, next_y = x + dx, y + dy
        if can_go(next_x, next_y, K):
            order -= 1
            ans[next_x][next_y] = order
            visited[next_x][next_y] = 1
            DFS(next_x, next_y, K)

Ks = find_max_K()
max_K = 1
answer = 0
for K in range(1, Ks+1):
    count_region = 0
    ans = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if can_go(row, col, K):
                order = -1
                ans[row][col] = order
                visited[row][col] = 1
                DFS(row, col, K)
    # print(ans)
    for i in range(N):
        for j in range(M):
            if ans[i][j] == -1:
                count_region += 1
    # print('count_region, answer', count_region, answer)
    if count_region > answer:
        max_K = K
    answer = max(answer, count_region)
print(max_K, answer)