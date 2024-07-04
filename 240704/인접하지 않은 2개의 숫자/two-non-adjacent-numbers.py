import sys

n = int(input())
arr = list(map(int, input().split()))

total_max = -sys.maxsize
for i in range(len(arr)):
    now_max = 0
    for j in range(i + 2, len(arr)):
        if i == len(arr) - 2:
            break
        else:
            now_max = arr[i] + arr[j]
        total_max = max(total_max, now_max)
print(total_max)