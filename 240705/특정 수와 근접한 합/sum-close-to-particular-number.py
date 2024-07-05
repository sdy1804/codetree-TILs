import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))

min_diff = sys.maxsize
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        val_sum = sum(arr)
        val_sum -= (arr[i] + arr[j])
        now_diff = abs(S - val_sum)
        min_diff = min(now_diff, min_diff)
print(min_diff)