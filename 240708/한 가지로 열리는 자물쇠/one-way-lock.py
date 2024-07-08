N = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if abs(i - arr[0]) <= 2 or abs(j - arr[1]) <= 2 or abs(k - arr[2]) <= 2:
                cnt += 1
print(cnt)