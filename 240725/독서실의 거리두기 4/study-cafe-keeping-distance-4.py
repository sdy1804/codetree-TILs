import sys

N = int(input())
arr = list(map(int, input()))

# 일단 0을 찾아서 2개의 1을 넣음
# 1을 넣은 상태에서 1간의 거리를 찾고, 거리가 최소인 값을 저장
# 최소값들 중에 최대값을 찾을 수 있도록 글로벌 최대값 저장

total_max_min = 0
for i in range(N):
    if arr[i] == 1:
        continue
    if arr[i] == 0:
        arr[i] = 1
    now_min_dist = sys.maxsize
    for j in range(len(arr)):
        for k in range(j+1, len(arr)):
            if arr[j] == 1 and arr[k] == 1:
                dist = abs(j - k)
                now_min_dist = min(now_min_dist, dist)
    arr[i] = 0
    total_max_min = max(now_min_dist, total_max_min)
print(total_max_min)