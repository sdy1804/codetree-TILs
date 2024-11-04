N = int(input())
nums = [0] + list(map(int, input().split()))

# dp[i] -> i보다 앞에 있는 원소들 중 a[i]보다 값이 작은 수열에 a[i]를 추가한 부분 수열 중 최대 부분 수열
# 점화식 = dp[i] = max(dp[j]+1)
# 초기 값 dp[0] = 0, nums[0] = 0

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))