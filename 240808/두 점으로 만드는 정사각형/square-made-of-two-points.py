x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

left_down_x = min(x1, a1)
right_top_x = max(x2, a2)
left_down_y = min(y1, b1)
right_top_y = max(y2, b2)
# print(left_down_x, right_top_x)
# print(left_down_y, right_top_y)

if (right_top_x - left_down_x)**2 > (right_top_y - left_down_y)**2:
    print((right_top_x - left_down_x)**2)
else:
    print((right_top_y - left_down_y)**2)