command = input()

x, y = 0, 0
direct = 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0] # 북쪽 기준

for i in range(len(command)):
    if command[i] == 'L':
        direct = (direct - 1 + 4) % 4
        # print(direct)
    elif command[i] == 'R':
        direct = (direct + 1) % 4
        # print(direct)
    else:
        x, y = x + dx[direct], y + dy[direct]
print(x, y)