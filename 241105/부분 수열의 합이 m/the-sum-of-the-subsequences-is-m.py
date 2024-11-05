import sys

INT_MAX = sys.maxsize

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))

dp = [0 for _ in range(m+1)]

def initialize():
    
    for i in range(1, m+1):
        dp[i] = INT_MAX
    dp[0] = 0

initialize()

for i in range(1, n+1):
    for j in range(m, 0, -1):
        if j >= nums[i]:
            dp[j] = min(dp[j], dp[j-nums[i]]+1)

if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])