n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

total_min = 1000
for i in range(1, arr[0][1] // 2 + 1):
    ok_num = True
    now_min = 1000
    now_num = i
    for j in range(n):
        i = i * 2
        # print(i)
        if i <= arr[j][0] or i >= arr[j][1]:
            ok_num = False
    if ok_num:
        now_min = now_num
    # print(now_min)
    total_min = min(now_min, total_min)
print(total_min)