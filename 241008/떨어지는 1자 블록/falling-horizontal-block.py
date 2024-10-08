n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 두번째 행부터 k~k+m-1에 1이 있는지 확인
# 1이 있으면 현재 행의 위치의 k~k-m+1을 1로 변경 후 탈출
# 1이 없으면 다음번째 행을 대상으로 k~k+m-1에 1이 있는지 확인
# 이를 반복

real_k = k-1

def is_there_one(r):
    for idx in range(real_k, real_k+m):
        if grid[r][idx] == 1:
            return True 
    return False

for row in range(1, n):
    if is_there_one(row):
        for index in range(real_k, real_k+m):
            grid[row-1][index] = 1
        break

for elem in grid:
    for i in elem:
        print(i, end=" ")
    print()