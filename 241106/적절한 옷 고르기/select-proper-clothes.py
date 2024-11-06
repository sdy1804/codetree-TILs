import sys

INT_MIN = -sys.maxsize

N, M = map(int, input().split())

s = [0 for _ in range(N+1)]
e = [0 for _ in range(N+1)]
v = [0 for _ in range(N+1)]

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

def initialize():
    for i in range(1, M+1):
        for j in range(1, N+1):
            dp[i][j] = INT_MIN

    # 첫날부터 입을 수 있는 옷들에 대한 dp 초기값 설정
    for j in range(1, N+1):
        if s[j] == 1:
            dp[1][j] = 0

for i in range(1, N+1):
    s[i], e[i], v[i] = list(map(int, input().split()))

initialize()

for i in range(2, M+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            if s[k] <= i-1 and i-1 <= e[k] and s[j] <= i and i <= e[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(v[j] - v[k]))
print(max(dp[M]))