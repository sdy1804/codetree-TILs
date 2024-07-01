N = int(input())
arr = [list(input().split()) for _ in range(N)]
K = int(input())

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

# K 값에 따라 쏘는 방향이 정해져야 함
# N = 2인 경우 - 1,2 / 3,4 / 5,6 / 7,8
# N = 3인 경우 - 1,2,3 / 4,5,6 / 7,8,9 / 10,11,12
# K <= N -> 위, N < K <= 2N -> 오른쪽, 2N < K <= 3N -> 아래, 3N < K <= 4N -> 왼쪽
# K - 1이 좌표상의 시작점 ex) 위면 arr[0][K-1], 오른쪽이면 arr[(K-1)%N][N-1], 아래면 arr[N-1][], 왼쪽이면 arr[][0]

# 위에서 쏨, '/'이면 -> 왼쪽으로 이동, 왼쪽이 in_range 없으면 끝, 있으면 카운트 +1
# 오른쪽에서 쏨, '/'이면 -> 아래로 이동, 아래가 in_range 없으면 끝, 있으면 카운트 +1

if K <= N:
    start_x, start_y = 0, K-1
    shoot_direct = 0 # 북쪽에서 들어옴
elif K > N and K <= 2*N:
    start_x, start_y = (K-1)%N, N-1
    shoot_direct = 1 # 동쪽에서 들어옴
elif K > 2*N and K <= 3*N:
    start_x, start_y = N-1, abs(K - 3*N)
    shoot_direct = 2 # 남쪽에서 들어옴
elif K > 3*N and K <= 4*N:
    start_x, start_y = abs(K - 4*N),0
    shoot_direct = 3 # 서쪽에서 들어옴
# print(start_x, start_y)
# print(arr[2][0][0])

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < N

cnt = 0
if arr[start_x][0][start_y] == '/' and shoot_direct == 0:
    nx, ny = start_x + dx[3], start_y + dy[3] # 서로 이동
    shoot_direct = 1 # 동에서 들어옴
    cnt += 1
elif arr[start_x][0][start_y] == '/' and shoot_direct == 1:
    nx, ny = start_x + dx[2], start_y + dy[2] # 남으로 이동
    shoot_direct = 0 # 북에서 들어옴
    cnt += 1
elif arr[start_x][0][start_y] == '/' and shoot_direct == 2:
    nx, ny = start_x + dx[1], start_y + dy[1] # 동으로 이동
    shoot_direct = 3 # 서에서 들어옴
    cnt += 1
elif arr[start_x][0][start_y] == '/' and shoot_direct == 3:
    nx, ny = start_x + dx[0], start_y + dy[0] # 북으로 이동
    shoot_direct = 2 # 남에서 들어옴
    cnt += 1

if arr[start_x][0][start_y] == '\\' and shoot_direct == 0:
    nx, ny = start_x + dx[1], start_y + dy[1] # 동으로 이동
    shoot_direct = 3 # 서에서 들어옴
    cnt += 1
elif arr[start_x][0][start_y] == '\\' and shoot_direct == 1:
    nx, ny = start_x + dx[0], start_y + dy[0] # 북으로 이동
    shoot_direct = 2 # 남에서 들어옴
    cnt += 1
elif arr[start_x][0][start_y] == '\\' and shoot_direct == 2:
    nx, ny = start_x + dx[3], start_y + dy[3] # 서로 이동
    shoot_direct = 1 # 동에서 들어옴
    cnt += 1
elif arr[start_x][0][start_y] == '\\' and shoot_direct == 3:
    nx, ny = start_x + dx[2], start_y + dy[2] # 남으로 이동
    shoot_direct = 0 # 북에서 들어옴
    cnt += 1

while in_range(nx, ny):
    if arr[nx][0][ny] == '/' and shoot_direct == 0:
        nx, ny = nx + dx[3], ny + dy[3] # 서로 이동
        shoot_direct = 1 # 동에서 들어옴
        cnt += 1
    elif arr[nx][0][ny] == '/' and shoot_direct == 1:
        nx, ny = nx + dx[2], ny + dy[2] # 남으로 이동
        shoot_direct = 0 # 북에서 들어옴
        cnt += 1
    elif arr[nx][0][ny] == '/' and shoot_direct == 2:
        nx, ny = nx + dx[1], ny + dy[1] # 동으로 이동
        shoot_direct = 3 # 서에서 들어옴
        cnt += 1
    elif arr[nx][0][ny] == '/' and shoot_direct == 3:
        nx, ny = nx + dx[0], ny + dy[0] # 북으로 이동
        shoot_direct = 2 # 남에서 들어옴
        cnt += 1

    elif arr[nx][0][ny] == '\\' and shoot_direct == 0:
        nx, ny = nx + dx[1], ny + dy[1] # 동으로 이동
        shoot_direct = 3 # 서에서 들어옴
        cnt += 1
    elif arr[nx][0][ny] == '\\' and shoot_direct == 1:
        nx, ny = nx + dx[0], ny + dy[0] # 북으로 이동
        shoot_direct = 2 # 남에서 들어옴
        cnt += 1
    elif arr[nx][0][ny] == '\\' and shoot_direct == 2:
        nx, ny = nx + dx[3], ny + dy[3] # 서로 이동
        shoot_direct = 1 # 동에서 들어옴
        cnt += 1
    elif arr[nx][0][ny] == '\\' and shoot_direct == 3:
        nx, ny = nx + dx[2], ny + dy[2] # 남으로 이동
        shoot_direct = 0 # 북에서 들어옴
        cnt += 1
print(cnt)