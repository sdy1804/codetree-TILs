N, B = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

P.sort()

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
        # print('j', j)
        # print('cnt', cnt)
        if i == j:
            P[j][0] = P[j][0] * 2
        # print('P', P)
    total_cnt = max(total_cnt, cnt)
print(total_cnt)

# 순서대로가 아니라 다른 순서도 있을듯함