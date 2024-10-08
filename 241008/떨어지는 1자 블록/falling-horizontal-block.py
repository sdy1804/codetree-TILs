n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 현재 행에서 다음 행 k~k+m-1에 1이 있는지 또는 끝자락인지 확인
# 1이 있으면 현재 행의 위치의 k~k-m+1을 1로 변경 후 탈출
# 1이 없으면 다음번째 행에서 그 다음 행 자리에 k~k+m-1에 1이 있는지 확인
# 이를 반복

real_k = k-1

def is_end(r):
    if r+1 == n:
        return True
    return False

def is_there_one(r):
    for idx in range(real_k, real_k+m):
        if grid[r+1][idx] == 1:
            return True 
    return False

for row in range(n):
    if is_end(row) or is_there_one(row):
        for index in range(real_k, real_k+m):
            grid[row][index] = 1
        break

for elem in grid:
    for i in elem:
        print(i, end=" ")
    print()