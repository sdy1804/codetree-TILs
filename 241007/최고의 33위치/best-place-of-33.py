N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 왼쪽 위를 기준으로 탐색
# 오른쪽 또는 아랫쪽이 벗어나는 순간 pass

def count_coins(r, c):
    num_of_coins = 0

    for rows in range(r, r+3):
        for columns in range(c, c+3):
            if grid[rows][columns] == 1:
                num_of_coins += 1

    return num_of_coins

ans = 0
for row in range(N):
    for column in range(N):    
        if column+2 >= N or row+2 >= N:
            continue

        now_coins = count_coins(row, column)
        ans = max(now_coins, ans)

print(ans)