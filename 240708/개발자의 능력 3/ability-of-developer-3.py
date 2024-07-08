import sys

arr = list(map(int, input().split()))

def get_diff(i, j, k):
    group1 = arr[i] + arr[j] + arr[k]
    group2 = sum(arr) - group1
    return abs(group1 - group2)

total_mindiff = sys.maxsize
for i in range(len(arr)):
    now_min = 0
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            now_min = get_diff(i, j, k)
            total_mindiff = min(total_mindiff, now_min)
print(total_mindiff)