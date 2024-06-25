N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

OFFSET = 0
for elem in arr:
    for i in elem:
        if i < OFFSET:
            OFFSET = i

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] += abs(OFFSET)
# print(arr)

sqr1 = [[0] * 210 for _ in range(210)]
for i in range(N):
    for j in range(arr[i][0], arr[i][2]):
        for k in range(arr[i][1], arr[i][3]):
            sqr1[j][k] = 1
# print(sqr1)

count = 0
for i in range(len(sqr1)):
    count += sqr1[i].count(1)
print(count)