import math

def lcm(N, M):
    num = (N * M) / math.gcd(N, M)
    print(int(num))

n, m = map(int, input().split())
lcm(n, m)