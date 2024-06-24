n = int(input())
arr = list(input().split() for _ in range(n))
for i in range(len(arr)):
    for j in range(1):
        arr[i][0] = int(arr[i][0])

ans = [0] * 3001
# ans = [0] * 30

start_point = 500
for i in range(len(arr)):
    if arr[i][1] == 'R':
        for j in range(start_point, start_point + arr[i][0]):
            ans[j] += 1
        start_point += arr[i][0]
    else:
        for j in range(start_point - 1, start_point - arr[i][0] - 1, -1):
            ans[j] += 1
        start_point -= arr[i][0]
# print(ans)
count = 0
for elem in ans:
    if elem >= 2:
        count += 1
print(count)