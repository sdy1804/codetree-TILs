n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0] # 북 = 0, 동 = 1, 서 = 2, 남 = 3

def in_range(x, y):
    return x > 0 and x <= n and y > 0 and y <= n

direct = {'U': 0, 'R': 1, 'L': 2, 'D': 3}
# print(3 - direct[d])

bef_x, bef_y = r, c
now_direct = d
for i in range(t):
    now_x, now_y = bef_x + dx[direct[now_direct]], bef_y + dy[direct[now_direct]]
    # print("bef", bef_x, bef_y)
    # print('now', now_x, now_y)
    if not in_range(now_x, now_y):
        now_x = bef_x
        now_y = bef_y
        direct[now_direct] = 3 - direct[now_direct]
    else:
        bef_x = now_x
        bef_y = now_y
print(now_x, now_y)