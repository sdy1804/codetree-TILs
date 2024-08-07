N = int(input())
arr = list(map(int, input()))

# 간격이 좁을수록 거리를 최대로 할 수 없음
# 간격이 가장 큰 곳을 찾아서 최대한 붙지 않게 넣어주는 것이 최대일 것
# 1. 간격이 가장 큰 곳 찾기
# 2. 해당 인덱스를 찾아서 두 인덱스의 절반에 해당하는 곳을 찾음
# 3. 해당 부분에 1을 넣고, 다시 최소 거리 탐색

far_dist = 0
for first in range(len(arr)): # 간격 가장 큰 곳 찾기
    if arr[first] == 1:
        for secd in range(first+1, len(arr)):
            if arr[secd] == 1:
                now_dist = secd - first
                far_dist = max(far_dist, now_dist)
                if now_dist == far_dist:
                    X_1, X_2 = first, secd
                break

insert_idx = (X_1 + X_2) // 2 # 간격 큰 곳에 1 넣기
arr[insert_idx] = 1

min_dist = 100000
for first in range(len(arr)): # 수정된 간격 찾기
    if arr[first] == 1:
        for secd in range(first+1, len(arr)):
            if arr[secd] == 1:
                now_dist = secd - first
                min_dist = min(min_dist, now_dist)
                break
print(min_dist)