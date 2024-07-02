N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0

for i in range(len(arr)):
    sums = 0
    for j in range(N-2):
        sums = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        max_cnt = max(max_cnt, sums)
print(max_cnt)