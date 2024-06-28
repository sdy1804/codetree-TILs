command = input()

x, y = 0, 0
direct = 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] # 북 동 남 서

time = 0
come_back = False
for i in range(len(command)):
    if command[i] == 'L':
        direct = (direct + 1) % 4
        time += 1
    elif command[i] == 'R':
        direct = (direct - 1 + 4) % 4
        time += 1
    else:
        x, y = x + dx[direct], y + dy[direct]
        time += 1
        # print(x, y)
        # print(time)
        if x == 0 and y == 0:
            print(time)
            come_back = True
            break

if come_back == False:
    print(-1)