n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 두 개의 직사각형을 잡고, 두 직사각형이 겹치지 않을 경우에만 합을 구함
# 그 중 최대인 합을 구함

board = [[0 for _ in range(m)] for _ in range(n)]

def check_board():
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False

def draw(x1, y1, x2, y2):
    for r in range(x1, x2+1):
        for c in range(y1, y2+1):
            board[r][c] += 1

def clear_board():
    for r in range(n):
        for c in range(m):
            board[r][c] = 0

def overlapped(x1, y1, x2, y2, x3, y3, x4, y4):
    clear_board()
    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)
    return check_board() # 겹치면 True

def rect_sum(x1, y1, x2, y2):
    val_sum = 0
    for r in range(x1, x2+1):
        for c in range(y1, y2+1):
            val_sum += grid[r][c]
    return val_sum

def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = -1000000
    # (i,j)(k,l)인 두번째 직사각형 서치, 겹치지 않는 경우 합을 구함
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not overlapped(x1, y1, x2, y2, i, j, k, l):
                        max_sum = max(max_sum, rect_sum(x1, y1, x2, y2) + rect_sum(i, j, k, l))
    return max_sum

def find_max_sum():
    # 첫번째 직사각형을 서치하여 find_max_sum_with_rect로 넘기기 위한 함수
    max_sum = -1000000
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    max_sum = max(max_sum, find_max_sum_with_rect(i, j, k, l))
    return max_sum

ans = find_max_sum()
print(ans)