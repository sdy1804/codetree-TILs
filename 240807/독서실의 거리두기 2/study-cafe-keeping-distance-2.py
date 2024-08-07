N = int(input())
arr = list(map(int, input()))

# 1과 1 사이의 거리를 측정하는 경우 - 최대 거리를 구한 절반이 거리가 될 것
# 그 외에 마지막 1부터 끝자리의 0까지의 0의 갯수를 새는 경우 - 뒤에서부터 센 인덱스의 차이의 절댓값이 거리가 될것
# 1. 1과 1사이의 최대 거리 및 해당하는 인덱스 체크
# 2. 만약 끝자리가 0일 경우 가장 끝자리의 1과의 거리를 구함
# 3. 1과 2의 거리를 비교, 더 큰 곳을 기준으로 1을 삽입
# 4. 탐색을 통해 거리 도출

dist_max = 0
X_1, X_2 = 0, 0
for first in range(N):
    now_dist = 0
    if arr[first] == 1:
        for secnd in range(first+1, N):
            if arr[secnd] == 1:
                now_dist = secnd - first
                dist_max = max(now_dist, dist_max)
                if now_dist == dist_max:
                    X_1, X_2 = first, secnd
                break
# print(dist_max)

insert_idx = (X_1 + X_2) // 2
temp_dist = insert_idx - X_1
# arr[insert_idx] = 1
# print(arr)

last_zero_dist = 0
if arr[-1] == 0:
    for idx in range(-1, -N-1, -1):
        if arr[idx] == 1:
            last_zero_dist = abs(-1 - idx)
            break
# print(last_zero_dist)

first_zero_dist = 0
if arr[0] == 0:
    for idx in range(N):
        if arr[idx] == 1:
            first_zero_dist = abs(0 - idx)
            break
# print(first_zero_dist)

if last_zero_dist > first_zero_dist and last_zero_dist > temp_dist:
    arr[-1] = 1
elif first_zero_dist > last_zero_dist and first_zero_dist > temp_dist:
    arr[0] = 1
else:
    arr[insert_idx] = 1
# print(arr)

dist_min = 100000
for first in range(N):
    now_dist = 0
    if arr[first] == 1:
        for secnd in range(first+1, N):
            if arr[secnd] == 1:
                now_dist = secnd - first
                dist_min = min(now_dist, dist_min)
                break
print(dist_min)