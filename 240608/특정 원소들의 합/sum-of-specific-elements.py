arr_2d = [list(map(int, input().split())) for i in range(4)]
sum = 0
for i in range(4):
    for j in range(i+1):
        sum += arr_2d[i][j]
print(sum)