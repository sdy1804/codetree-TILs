N, B = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

def p_sum(lst):
    val_sum = 0
    for i in range(len(lst)):
        val_sum += lst[i][0]
    return val_sum

total_cnt = 0
for i in range(N):
    sums = 0
    cnt = 0
    for j in range(N):
        if i == j:
            P[j][0] = P[j][0] // 2
        sums += P[j][0]
        # print('sums',sums)
        if sums <= B:
            cnt += 1
        # print(cnt)
        if i == j:
            P[j][0] = P[j][0] * 2
        # print(P)
    total_cnt = max(total_cnt, cnt)
print(total_cnt)