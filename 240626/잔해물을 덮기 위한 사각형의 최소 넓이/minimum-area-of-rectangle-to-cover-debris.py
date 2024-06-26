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

set_column = 2100
ans = [[0] * set_column for _ in range(set_column)]

for i in range(sqr1[0], sqr1[2]):
    for j in range(sqr1[1], sqr1[3]):
        ans[i][j] = 1

for i in range(sqr2[0], sqr2[2]):
    for j in range(sqr2[1], sqr2[3]):
        ans[i][j] = 2
# print(ans)
row, max_column= 0, 0
for i in range(len(ans)):
    if 1 in ans[i]:
        row += 1
    first_column, last_column = 0, 0
    for j in range(0, len(ans[i])):
        if ans[i][j] == 1:
            first_column = j
            break
    for j in range(len(ans[i]) - 1, -1, -1):
        if ans[i][j] == 1:
            last_column = j
            break
    now_column = last_column - first_column + 1
    if now_column > max_column:
        max_column = now_column

print(max_column * row)