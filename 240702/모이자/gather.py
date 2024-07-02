import sys

n = int(input())
arr = list(map(int, input().split()))

min_sum = sys.maxsize
for i in range(len(arr)):
    sum_diff = 0
    for j in range(len(arr)):
        sum_diff += arr[j] * abs(i - j)
    min_sum = min(min_sum, sum_diff)
print(min_sum)