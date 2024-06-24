n = int(input())
arr = list(input().split() for _ in range(n))
for i in range(len(arr)):
    arr[i][0] = int(arr[i][0])

ans = [0] * 100 * 1000 * 2

# 검은색 = 1, 흰색 = 2
start_point = 100000
for i in range(len(arr)):
    if arr[i][1] == 'R':
        for j in range(start_point, start_point + arr[i][0]):
            ans[j] = 1
        start_point = start_point + arr[i][0] - 1
    else:
        for j in range(start_point, start_point - arr[i][0], -1):
            ans[j] = 2
        start_point = start_point - arr[i][0] + 1
print(ans.count(2), ans.count(1))