import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def find_dist(a, b, c, d):
    return (a - b)**2 + (c - d)**2

total_min = sys.maxsize
for i in range(n):
    for j in range(i + 1, n):
        now_min = find_dist(arr[i][0], arr[j][0], arr[i][1], arr[j][1])
    total_min = min(now_min, total_min)
print(total_min)