import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 최솟값 a일 때, 모든 수가 [a, a+k]이어야 함

total_min_cost = sys.maxsize
for a in range(0, max(arr)+1):
    now_cost = 0
    # print("최소값 범위", a, a+k)
    for i in range(len(arr)):
        if arr[i] < a or arr[i] > a+k:
            if arr[i] < a:
                now_cost += abs(arr[i] - a)
                # print('arr[i], a, cost', arr[i], a, now_cost)
            elif arr[i] > a+k:
                now_cost += abs(k - arr[i] + a)
                # print('arr[i], a, cost', arr[i], a, now_cost)
    total_min_cost = min(total_min_cost, now_cost)
print(total_min_cost)

# k = arr[i] - a + x
# 2 = 6 - 0 + x
# x = 2 - 6 + 0
# x = k - arr[i] + a