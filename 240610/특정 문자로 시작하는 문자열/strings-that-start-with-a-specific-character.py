n = int(input())
arr = [input() for _ in range(n)]
alpha = input()
cnt = 0
len_sum = 0

for i in range(len(arr)):
    if arr[i][0] == alpha:
        cnt += 1
        len_sum += len(arr[i])
avg = len_sum / cnt
print(cnt, f"{avg:.2f}")