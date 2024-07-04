import sys

N = int(input())
people = [int(input()) for _ in range(N)]

min_dist = sys.maxsize
for i in range(len(people)):
    weight = [0] * len(people)
    now_dist = 0
    for j in range(i + 1, len(people)):
        weight[j] = weight[j-1] + 1
    if weight[i-1] == 0:
        for k in range(0, i):
            if k == 0:
                weight[k] += weight[len(people) - 1] + 1
            else:
                weight[k] += weight[k-1] + 1
    # print(weight)
    for l in range(len(people)):
        now_dist += people[l] * weight[l] 
    # print(now_dist)
    min_dist = min(min_dist, now_dist)
print(min_dist)

# 현재 위치(i)를 기준으로 누적거리를 쌓아가는 방법
# 1부터 할 때 거리: 0, 1, 2, 3, 4 -> i = 0
# 2부터 할 때 거리: 4, 0, 1, 2, 3 -> i = 1
# 3부터 할 때 거리: 3, 4, 0, 1, 2 -> i = 2
# 4부터 할 때 거리: 2, 3, 4, 0, 1 -> i = 3
# 5부터 할 때 거리: 1, 2, 3, 4, 0 -> i = 4
# i 위치부터 people의 끝까지 0부터 채움
# 만약 people의 처음부터 i 이전까지 값들이 0 이라면,
# 맨 끝값에서 +1을 해서 시작하여 i 이전까지 채움