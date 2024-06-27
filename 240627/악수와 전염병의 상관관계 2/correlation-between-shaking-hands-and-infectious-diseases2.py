# K = 감염자가 다른 사람 감염시킬 수 있는 횟수
# P = 처음 감염자 번호
# T = 개발자 간의 악수 횟수
N, K, P, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(T)]

infest_count = [0] * N
check_infested = [0] * N
check_infested[P-1] = 1

arr.sort(key = lambda arr: arr[0])

for i in range(len(arr)):
    if check_infested[arr[i][1] - 1] == 1 and check_infested[arr[i][2] - 1] == 0:
        if infest_count[arr[i][1] - 1] < K: 
            check_infested[arr[i][2] - 1] = 1  # 감염 안된 사람 감염 표시
            infest_count[arr[i][1] - 1] += 1  # 감염시킨 사람 감염시킨 횟수 증가
        else:
            infest_count[arr[i][1] - 1] += 1
    elif check_infested[arr[i][1] - 1] == 0 and check_infested[arr[i][2] - 1] == 1:
        if infest_count[arr[i][2] - 1] < K:
            check_infested[arr[i][1] - 1] = 1
            infest_count[arr[i][2] - 1] += 1
        else:
            infest_count[arr[i][2] - 1] += 1
    elif check_infested[arr[i][1] - 1] == 1 and check_infested[arr[i][2] - 1] == 1:
        infest_count[arr[i][1] - 1] += 1
        infest_count[arr[i][2] - 1] += 1
# print(check_infested)
# print(infest_count)
for elem in check_infested:
    print(elem, end="")