def print_one(N, M):
    for _ in range(N):
        print("1"*M)


n, m = map(int, input().split())
print_one(n, m)