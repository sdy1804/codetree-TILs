N = int(input())

memo = [-1 for _ in range(N+1)]

def fibo(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

fibo(N)
print(memo[N])