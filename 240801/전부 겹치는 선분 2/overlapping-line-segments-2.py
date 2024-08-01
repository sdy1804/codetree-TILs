n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr2 = arr.copy()

ans = False
for i in range(n):
    start_max = 0
    last_min = 10000
    arr.remove(arr[i])
    for j in range(len(arr)):
        start_max = max(start_max, arr[j][0])
        last_min = min(last_min, arr[j][1])
    if start_max <= last_min:
        ans = True
        break
    else:
        ans = False
    arr = arr2.copy()

if ans:
    print('Yes')
else:
    print('No')