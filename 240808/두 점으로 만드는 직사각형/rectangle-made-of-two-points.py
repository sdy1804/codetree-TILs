x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

if x1 < a1:
    left_down_x = x1
else:
    left_down_x = a1

if y1 < b1:
    left_down_y = y1
else:
    left_down_y = b1

if x2 < a2:
    right_top_x = a2
else:
    right_top_x = x2

if y2 < b2:
    right_top_y = b2
else:
    right_top_y = y2

# print(left_down_x, left_down_y, right_top_x, right_top_y)
print((right_top_x - left_down_x) * (right_top_y - left_down_y))