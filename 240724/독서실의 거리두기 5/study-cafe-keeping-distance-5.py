N = int(input())
arr = list(map(int, input()))
# print(arr)
# 0인 곳에 1을 넣을 경우의 1간의 최소 거리를 구하기
# 그중 최대값 찾기

total_max_min = 0
for i in range(N): # 하나씩 0을 1로 바꿈
    now_min = 1000
    if arr[i] == 0:
        arr[i] = 1
    else:
        continue
    # print(arr)
    now_dist = 1000
    for j in range(N): # 탐색하면서 1간의 거리 구함
        if arr[j] == 1:
            for k in range(j+1, N):
                if arr[k] == 1:
                    now_dist = abs(j-k)
                # print('j, k', j, k)
                # print('now_dist', now_dist)
                now_min = min(now_min, now_dist)
                # print('now_min', now_min)
    arr[i] = 0
    total_max_min = max(total_max_min, now_min)
    # print(arr)
    # print(now_min)
print(total_max_min)