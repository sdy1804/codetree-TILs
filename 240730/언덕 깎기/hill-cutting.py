import sys

N = int(input())
arr = [int(input()) for _ in range(N)]

K = 17
# 모든 숫자들이 최대 최소 차이가 17이하여야 함
# 최소값을 정해서 완전탐색
# 해당 최소값에 따른 비용 계산

def cal_cost(lst, mins):
    cost = 0
    for i in range(len(lst)):
        if lst[i] < mins:
            cost += (mins - lst[i])**2
        elif lst[i] > mins + K:
            cost += (lst[i] - (mins + K))**2
    return cost

total_min_cost = sys.maxsize
for i in range(0, 101):
    now_cost = cal_cost(arr, i)
    total_min_cost = min(now_cost, total_min_cost)
print(total_min_cost)