N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 1. 만들 수 있는 리스트의 조합을 완탐해서 min, max?
# 2. 최대 최소값을 하나씩 찝은후, 최대 최소와의 값 차이가 K 이하면 나머지 숫자들을 탐색
# 탐색하면서 최대 최소값을 제외한 나머지가 차이를 구했을 때 K 이하이면 append
# 3. 위 방법 시간 초과 - 원소 하나 기준으로 K 이하면 append
total_max_len = 0
for i in range(N):
    temp_list = []
    now_max_len = 0
    now_min, now_max = arr[i], arr[i]
    temp_list.append(now_min)
    for j in range(i+1, N):
        if abs(arr[j] - now_min) <= K and abs(arr[j] - now_max) <= K:
            temp_list.append(arr[j])
            now_min = min(temp_list)
            now_max = max(temp_list)
            # print(temp_list)
            now_max_len = len(temp_list)
            # print(now_max_len)
            total_max_len = max(now_max_len, total_max_len)
print(total_max_len)