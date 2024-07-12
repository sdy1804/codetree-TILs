N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def tri_area(x1, x2, x3, y1, y2, y3):
    if (x1 == x2 or x1 == x3 or x2 == x3) and (y1 == y2 or y1 == y3 or y2 == y3):
        return abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)) / 2
    else:
        return 0

total_max = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            now_max = tri_area(arr[i][0], arr[j][0], arr[k][0], arr[i][1], arr[j][1], arr[k][1])
            # print(now_max)
            total_max = max(now_max, total_max)
print(int(total_max * 2))