n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = [0] * 100

for i in range(len(arr)):
    for j in range(arr[i][0], arr[i][1]+1):
        ans[j] += 1
print(max(ans))