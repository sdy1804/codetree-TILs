n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1. K를 0부터 n-1까지 바꿔가며 마름모 꼴로 전체 좌표를 탐색 -> K를 바꿨을 때 손해 여부 확인, 갱신
# 2. 좌표를 이동하며 또 다시 K 변경, 갱신
# 3. 해당 최대값 출력

# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < n

# def rhombus(x, y, K):
#     grid_rhombus = [[0 for _ in range(n)] for _ in range(n)]
    
#     for i in range(1, K+1):
#         # print(K - i)
#         # 상
#         if in_range(x-i, y+(K-i)):
#             for j in range(K-i+1):
#                 grid_rhombus[x-i][y+j] = 1
#         if in_range(x-i, y-(K-i)):
#             for j in range(K-i+1):
#                 grid_rhombus[x-i][y-j] = 1
#         if in_range(x-i, y):
#             grid_rhombus[x-i][y] = 1
#         # 하
#         if in_range(x+i, y+(K-i)):
#             for j in range(K-i+1):
#                 grid_rhombus[x+i][y+j] = 1
#         if in_range(x+i, y-(K-i)):
#             for j in range(K-i+1):
#                 grid_rhombus[x+i][y-j] = 1
#         if in_range(x+i, y):
#             grid_rhombus[x+i][y] = 1
#         # 좌
#         if in_range(x+(K-i), y-i):
#             for j in range(K-i+1):
#                 grid_rhombus[x+j][y-i] = 1
#         if in_range(x-(K-i), y-i):
#             for j in range(K-i+1):
#                 grid_rhombus[x-j][y-i] = 1
#         if in_range(x, y-i):
#             grid_rhombus[x][y-i] = 1
#         # 우
#         if in_range(x+(K-i), y+i):
#             for j in range(K-i+1):
#                 grid_rhombus[x+j][y+i] = 1
#         if in_range(x-(K-i), y+i):
#             for j in range(K-i+1):
#                 grid_rhombus[x-j][y+i] = 1
#         if in_range(x, y+i):
#             grid_rhombus[x][y+i] = 1
#         # 중앙
#         grid_rhombus[x][y] = 1
    
#     if K == 0:
#         grid_rhombus[x][y] = 1

#     return grid_rhombus

def cal_area(K):
    return K * K + (K+1) * (K+1)

def num_gold(x, y, k):
    global grid
    num_of_gold = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] and abs(x-r) + abs(y-c) <= k: # 중심좌표와의 거리가 k 이내이면 마름모 범위 내에 해당
                num_of_gold += 1
    return num_of_gold

ans = 0

for row in range(n):
    for column in range(n):
        for k in range(2*(n-1) + 1):
            if num_gold(row, column, k) * m >= cal_area(k):
                ans = max(ans, num_gold(row, column, k))

print(ans)