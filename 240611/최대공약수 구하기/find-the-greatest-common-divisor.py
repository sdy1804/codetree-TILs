def gcd(N, M):
    if N > M:
        for i in range(1, N+1):
            if N % i == 0 and M % i == 0:
                ans = i
    else:
        for i in range(1, M+1):
            if N % i == 0 and M % i == 0:
                ans = i
    print(ans)

n, m = map(int, input().split())
gcd(n, m)