import sys

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

def Man_distance(arr1, arr2):
    dist = abs(arr1[0] - arr2[0]) + abs(arr1[1] - arr2[1])
    return dist

min_dist = sys.maxsize
for i in range(1, len(points) - 1): # 1, 2, 3
    now_dist = 0
    copy_points = points
    # print(copy_points)
    for j in range(1, len(points) - 1): # 1, 2, 3
        if i == j:
            idx = j
            removed_elem = copy_points.pop(j)
        # print(copy_points)
        now_dist += Man_distance(copy_points[j-1], copy_points[j])
        # print(now_dist)
    min_dist = min(min_dist, now_dist)
    copy_points.insert(idx, removed_elem)
print(min_dist)

# 3번째 꺼 빼고 계산 시,  0 0이랑 8 3이랑 계산 안하고, 그 앞인 11 -1이 3 5랑 계산함
# 아예 리스트에서 뺐다가 넣는게 나을지 고민 필요