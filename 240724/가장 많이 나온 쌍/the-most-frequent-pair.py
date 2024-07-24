n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

total_max_cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        now_cnt = 0
        for k in range(len(arr)):
            if (i == arr[k][0] or i == arr[k][1]) and (j == arr[k][0] or j == arr[k][1]):
                # print('i, j', i, j)
                # print('arr[k]', arr[k])
                now_cnt += 1
        total_max_cnt = max(now_cnt, total_max_cnt)
print(total_max_cnt)