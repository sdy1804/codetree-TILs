start, end = map(int, input().split())
ans = 0

for i in range(start, end+1):
    sum_cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            sum_cnt += 1
    if sum_cnt == 3:
        ans += 1
print(ans)