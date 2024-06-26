sqr1 = list(map(int, input().split()))
sqr2 = list(map(int, input().split()))

OFFSET = 0
for i in range(len(sqr1)):
    if int(sqr1[i]) < OFFSET:
        OFFSET = sqr1[i]
    if sqr2[i] < OFFSET:
        OFFSET = sqr2[i]

for i in range(len(sqr1)):
    sqr1[i] += abs(OFFSET)
    sqr2[i] += abs(OFFSET)


ans = [[0] * 2100 for _ in range(2100)]

for i in range(sqr1[0], sqr1[2]):
    for j in range(sqr1[1], sqr1[3]):
        ans[i][j] = 1

for i in range(sqr2[0], sqr2[2]):
    for j in range(sqr2[1], sqr2[3]):
        ans[i][j] = 2

column, max_row = 0, 0
for i in range(len(ans)):
    if 1 in ans[i]:
        column += 1
    now_row = 0
    for j in range(len(ans[i])):
        if ans[i][j] == 1:
            now_row += 1
    if now_row > max_row:
        max_row = now_row

print(max_row * column)