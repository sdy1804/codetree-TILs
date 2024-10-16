n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1. K를 0부터 n-1까지 바꿔가며 전체 좌표를 탐색 ex) 예시에서는 0 ~ 4까지 탐색
# 마름모 형태로 어떻게 탐색할지? -> K - (0 ~ K-1)의 값을 다른 좌표에 부과하는 방식
# 또는 K값에 따른 행 및 열 값 추가 -> ex) K = 2일 때, K+1행 좌표에서 각 열에 +1, K+2행에서 각 열에 +0
# ex) K = 3일 때, K+1행 좌표에서 각 열에 +2, K+2행은 각 열에 +1, K+3행은 각 열에 +0
# 2. 매 좌표마다 금의 최대 갯수를 갱신 -> 만약 손해라면 갱신하지 않음
# 3. 해당 최대값 출력

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def rhombus(x, y, K):
    grid_rhombus = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(1, K+1):
        # print(K - i)
        # 상
        if in_range(x-i, y+(K-i)):
            for j in range(K-i+1):
                grid_rhombus[x-i][y+j] = 1
        if in_range(x-i, y-(K-i)):
            for j in range(K-i+1):
                grid_rhombus[x-i][y-j] = 1
        if in_range(x-i, y):
            grid_rhombus[x-i][y] = 1
        # 하
        if in_range(x+i, y+(K-i)):
            for j in range(K-i+1):
                grid_rhombus[x+i][y+j] = 1
        if in_range(x+i, y-(K-i)):
            for j in range(K-i+1):
                grid_rhombus[x+i][y-j] = 1
        if in_range(x+i, y):
            grid_rhombus[x+i][y] = 1
        # 좌
        if in_range(x+(K-i), y-i):
            for j in range(K-i+1):
                grid_rhombus[x+j][y-i] = 1
        if in_range(x-(K-i), y-i):
            for j in range(K-i+1):
                grid_rhombus[x-j][y-i] = 1
        if in_range(x, y-i):
            grid_rhombus[x][y-i] = 1
        # 우
        if in_range(x+(K-i), y+i):
            for j in range(K-i+1):
                grid_rhombus[x+j][y+i] = 1
        if in_range(x-(K-i), y+i):
            for j in range(K-i+1):
                grid_rhombus[x-j][y+i] = 1
        if in_range(x, y+i):
            grid_rhombus[x][y+i] = 1
        # 중앙
        grid_rhombus[x][y] = 1
    
    if K == 0:
        grid_rhombus[x][y] = 1

    return grid_rhombus

def cal_gold_num(x, y, grid):
    global m
    max_gold_num = 0

    for k in range(0, n):
        now_rhombus = rhombus(x, y, k)
        now_gold_num = 0
        for r in range(n):
            for c in range(n):
                if now_rhombus[r][c] == 1 and grid[r][c] == 1:
                    now_gold_num += 1
        if now_gold_num * m >= k * k + (k+1) * (k+1):
            max_gold_num = max(now_gold_num, max_gold_num)
    
    return max_gold_num

ans = 0

for row in range(n):
    for column in range(n):
        total_now_gold = cal_gold_num(row, column, grid)
        ans = max(total_now_gold, ans)

print(ans)