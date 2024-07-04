N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1] # 동, 남, 서, 북

# L을 탐색 중에 찾으면, L을 기준으로 주변에 E가 있는지 탐색, 범위를 벗어나면 빠져나오가
# 이동한 E에서 현재 방향에서 E가 있으면 카운트
# 없으면 빠져나오기

def in_range(x, y):
    return x >= 0 and x < N and y >= 0 and y < M

cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 'L':
            # print("L 위치", i, j)
            for dxs, dys in zip(dx, dy):
                cur_x, cur_y = i, j
                nx, ny = cur_x + dxs, cur_y + dys
                if not in_range(nx, ny):
                    # print("범위 초과")
                    continue
                # print("현재 주변 알파벳들", arr[nx][ny])
                if arr[nx][ny] == 'E':
                    # print(dxs, dys)
                    cur_x, cur_y = nx, ny
                    nx, ny = cur_x + dxs, cur_y + dys
                    if not in_range(nx, ny):
                        # print("범위 초과")
                        continue
                    if arr[nx][ny] == 'E':
                        # print('최종점', arr[nx][ny], nx, ny)
                        cnt += 1
                    # else:
                        # print("LEE 아님")
                        
print(cnt)