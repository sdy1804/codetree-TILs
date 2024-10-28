n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 일단 모든 크기의 직사각형을 탐색
# 탐색 후 직사각형 내에 음수 값이 있는지 없는지 체크
# 없다면 직사각형의 크기를 반환, 최대 크기를 찾음

# 직사각형 내에 음수가 있는지 체크, 있으면 True
def check_minus_val(x1, y1, x2, y2):
    for r in range(x1, x2+1):
        for c in range(y1, y2+1):
            if grid[r][c] <= 0:
                return True
    return False

# 직사각형 크기를 구하는 함수
def cal_rect_size(x1, y1, x2, y2):
    return (x2-x1+1) * (y2-y1+1)

# 전체에서 직사각형의 크기 및 시작좌표(왼쪽위)를 바꿔가며 탐색, 최대값 갱신
def search_max_rect():
    max_size = -10000

    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not check_minus_val(i, j, k, l):
                        max_size = max(max_size, cal_rect_size(i, j, k, l))
    return max_size

ans = search_max_rect()
if ans <= 0:
    print(-1)
else:
    print(ans)