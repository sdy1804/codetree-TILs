n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

lowest, biggest = 10000, 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        lowest = min(lowest, arr[i][j])
        biggest = max(biggest, arr[i][j])

Pos = False
for point in range(lowest, biggest+1):
    # print('point', point)
    # print('Pos', Pos)
    for i in range(len(arr)):
        if arr[i][0] <= point and arr[i][1] >= point:
            Pos = True
            # print('postive Pos', Pos)
        else:
            Pos = False
            # print('neg Pos', Pos)
            break
    if Pos:
        break

if Pos:
    print('Yes')
else:
    print('No')