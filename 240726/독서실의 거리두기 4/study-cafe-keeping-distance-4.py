import sys

N = int(input())
arr = list(map(int, input()))

# 일단 0을 찾아서 2개의 1을 넣음
# 1을 넣은 상태에서 1간의 거리를 찾고, 현재 세팅값에서 거리가 최소인 값을 저장
# 현재 세팅값의 최소값과 글로벌 최대값을 비교해서 최대값 찾음

total_max_min = 0
for i in range(N):
    if arr[i] == 1:
        continue
    if arr[i] == 0:
        arr[i] = 1
    for j in range(i+1, N):
        if arr[j] == 1:
            continue
        if arr[j] == 0:
            arr[j] = 1
        # print(arr)
        now_min = sys.maxsize
        for k in range(N):
            now_dist = 0
            if arr[k] == 1:
                for l in range(k+1, N):
                    if arr[l] == 1:
                        now_dist = abs(k - l)
                        # print('k, l', k, l)
                        now_min = min(now_dist, now_min)
                        # print('now_min', now_min)
                        break
        total_max_min = max(now_min, total_max_min)
        # print('total_max_min', total_max_min)
        arr[j] = 0
    arr[i] = 0
print(total_max_min)