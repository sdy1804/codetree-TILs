N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 완탐으로 쌍을 만듦
# 만약 두 쌍이 같고, K범위 안이면 max값으로 저장
# 새롭게 같은 두쌍이 발생하면 max값 갱신
total_max = -100
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        now_max = 0
        if arr[i] == arr[j] and j - i <= K:
            now_max = arr[i]
        else:
            now_max = -1
        # print(now_max)
        total_max = max(total_max, now_max)
print(total_max)