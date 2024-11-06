import sys

INT_MIN = -sys.maxsize

n = int(input())
nums = [0] + list(map(int, input().split()))

dp = [INT_MIN for _ in range(n+1)]
dp[1] = nums[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-1] + nums[i], nums[i])

print(max(dp))