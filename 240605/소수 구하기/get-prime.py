n = int(input())

for i in range(2, n+1):
    sum_cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            sum_cnt += 1
    if sum_cnt == 2:
        print(i, end=" ")