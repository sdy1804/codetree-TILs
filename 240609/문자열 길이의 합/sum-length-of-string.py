n = int(input())
arr = [input() for _ in range(n)]
len_sum = 0
cnt = 0

for i in range(len(arr)):
    len_sum += len(arr[i])
    if arr[i][0] == 'a':
        cnt += 1
print(len_sum, cnt)