n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 100000
for i in range(n):
    now_nums = arr[i]
    arr.remove(arr[i])
    # print(arr)
    val_max, val_min = 0, 100000
    for j in range(len(arr)):
        val_min = min(val_min, arr[j][0])
        val_max = max(val_max, arr[j][1])
    length = val_max - val_min
    ans = min(length, ans)
    arr.insert(i, now_nums)
    # print(arr)
print(ans)