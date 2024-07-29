import sys

N = int(input())
arr = [int(input()) for _ in range(N)]

# 1. min, max로 현재 최대, 최소값 뽑아내기
# 2. 최소비용을 찾기 위해 두 값의 차이값을 구한후 변화량을 바꿔가며 값을 계산
# 3. 최소비용의 변화량으로 값들을 변경 후, 변화량에 대한 소비값은 저장
# 4. 새로운 min, max의 차이가 17이하인지 확인

now_min, now_max = min(arr), max(arr)
now_min_idx, now_max_idx = arr.index(now_min), arr.index(now_max)
# print('first now_min, now_max', now_min, now_max)
# print('first now_min_idx, now_max_idx', now_min_idx, now_max_idx)

ans = 0
while abs(now_min - now_max) > 17:
    now_diff = abs(now_min - now_max)
    # print('now_diff', now_diff)
    diff_to_17 = now_diff - 17
    # print('diff_to_17', diff_to_17)
    
    min_cost = sys.maxsize
    for i in range(diff_to_17+1):
        other_cost = diff_to_17 - i
        # print('other_cost', other_cost)
        now_min_cost = i * i + other_cost * other_cost
        # print('now_min_cost', now_min_cost)
        min_cost = min(now_min_cost, min_cost)
        if min_cost == now_min_cost:
            to_change_min = i
            to_change_max = other_cost
    ans += min_cost
    arr[now_min_idx] = arr[now_min_idx] + to_change_min
    arr[now_max_idx] = arr[now_max_idx] - to_change_max
    # print('min_cost', min_cost)
    # print('change arr', arr)

    now_min, now_max = min(arr), max(arr)
    # print('now_min, now_max', now_min, now_max)
    now_min_idx, now_max_idx = arr.index(now_min), arr.index(now_max)

print(ans)