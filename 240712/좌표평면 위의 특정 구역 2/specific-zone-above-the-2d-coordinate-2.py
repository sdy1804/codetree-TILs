import sys

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total_min_area = sys.maxsize
for i in range(N):
    total_max_x = 0
    total_min_x = sys.maxsize
    total_max_y = 0
    total_min_y = sys.maxsize
    for j in range(N):
        if i == j:
            continue
        now_x = arr[j][0]
        now_y = arr[j][1]
        total_max_x = max(total_max_x, now_x)
        total_min_x = min(total_min_x, now_x)
        total_max_y = max(total_max_y, now_y)
        total_min_y = min(total_min_y, now_y)
    now_area = (total_max_x - total_min_x) * (total_max_y - total_min_y)
    total_min_area = min(total_min_area, now_area)
print(total_min_area)