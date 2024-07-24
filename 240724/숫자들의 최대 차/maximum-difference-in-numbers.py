N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 1. 만들 수 있는 리스트의 조합을 완탐해서 min, max?
# 2. 최대 최소값을 하나씩 찝은후, 최대 최소와의 값 차이가 K 이하면 나머지 숫자들을 탐색
# 탐색하면서 최대 최소값을 제외한 나머지가 차이를 구했을 때 K 이하이면 append

for i in range(N):
    for j in range(i+1, N):
        temp_list = []
        if abs(arr[i] - arr[j]) <= 3:
            now_min = min(arr[i], arr[j])
            now_max = max(arr[i], arr[j])
            temp_list.append(now_min)
            temp_list.append(now_max)
            for k in range(N):
                # print(arr[i], arr[j])
                if (k == i or k == j):
                    continue
                if abs(arr[k] - now_min) <= 3 and abs(arr[k] - now_max) <= 3:
                    temp_list.append(arr[k])
# print(temp_list)
print(len(temp_list))