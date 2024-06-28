N = int(input())
arr = [list(input().split()) for _ in range(N)]
for i in range(len(arr)):
    arr[i][1] = int(arr[i][1])

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

direct = {'N': 0, 'E': 1, "S": 2, "W": 3}

x, y = 0, 0
time = 0
start_point = False
for i in range(N):
    for j in range(arr[i][1]):
        x, y = x + dx[direct[arr[i][0]]], y + dy[direct[arr[i][0]]]
        time += 1
        if x == 0 and y == 0:
            print(time)
            start_point = True
            break

if start_point == False:
    print(-1)