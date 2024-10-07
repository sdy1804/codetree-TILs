n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 격자의 개념으로 접근 -> 2개의 격자 형태
# 행에서의 격자(크기 1 X m), 열에서의 격자(크기 m X 1)
# 격자에서 두 숫자가 같다면 ans + 1
dup_list_row = []
dup_list_col = []

def check_column(r, c, m):
    for i in range(1, m): # 1, 2
        if grid[r+i-1][c] != grid[r+i][c]:
            return 0
    if c not in dup_list_col:
        dup_list_col.append(c)
    # return 1

def check_row(r, c, m):
    for i in range(1, m): # 1, 2
        if grid[r][c+i-1] != grid[r][c+i]:
            return 0
    if r not in dup_list_row:
        dup_list_row.append(r)
    # return 1

ans = 0
for row in range(n):
    for column in range(n):
        # print(row, column)
        # print(dup_list_row, dup_list_col)
        if row+m-1 < n:
            check_column(row, column, m)
        if column+m-1 < n:
            check_row(row, column, m)
ans += len(dup_list_row)
ans += len(dup_list_col)
print(ans)