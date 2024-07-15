N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 완탐으로 K까지의 쌍을 만듦
# 만약 두 쌍이 같다면 max값으로 저장
# 새롭게 같은 두쌍이 발생하면 max값 갱신
total_max = 0
for i in range(N - K):
    for j in range(i + 1, i + K + 1):
        now_max = 0
        # print(i, j)
        if arr[i] == arr[j]:
            now_max = arr[i]
        # print(now_max)
        total_max = max(total_max, now_max)
print(total_max)