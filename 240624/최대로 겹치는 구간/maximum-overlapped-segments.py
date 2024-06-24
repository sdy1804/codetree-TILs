n = int(input())
arr = list(input().split() for _ in range(n))
for i in range(len(arr)):
    for j in range(2):
        arr[i][j] = int(arr[i][j])

small = 0
for i in range(len(arr)):
    for j in range(2):
        if arr[i][j] < small:
            small = arr[i][j]

for i in range(len(arr)):
    for j in range(2):
        arr[i][j] += abs(small)
# print(arr)
ans = [0] * 201

for i in range(len(arr)):
    for j in range(arr[i][0], arr[i][1]):
        ans[j] += 1
print(max(ans))