N, K = map(int, input().split())
arr = list(input().split() for _ in range(K))

ans = [0] * N

for i in range(len(arr)):
    for j in range(int(arr[i][0])-1, int(arr[i][1])):
        ans[j] += 1

print(max(ans))