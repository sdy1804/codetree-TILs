import sys

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

# x, y 둘 다 0 ~ 100까지 완탐
# 완탐을 하는 과정에서 범위 지정을 통한 갯수 측정
# 범위에서 최대 갯수가 가장 적은 값을 갱신

total_min = sys.maxsize
for i in range(0, 101, 2):
    for j in range(0, 101, 2):
        points_max, left_down, left_up, right_down, right_up = 0, 0, 0, 0, 0
        for k in range(len(arr)):
            x, y = arr[k][0], arr[k][1]
            if x < i and y < j:
                left_down += 1
                # print('left_down, x, y', left_down, x, y)
            if x < i and y > j:
                left_up += 1
                # print('left_up, x, y', left_up, x, y)
            if x > i and y < j:
                right_down += 1
                # print('right_down, x, y', right_down, x, y)
            if x > i and y > j:
                right_up += 1
                # print('right_up, x, y', right_up, x, y)
        points_max = max(left_down, left_up, right_down, right_up)
        # print(points_max)
        total_min = min(points_max, total_min)
print(total_min)