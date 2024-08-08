x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

left_down_x = min(x1, a1)
right_top_x = max(x2, a2)
# print(left_down_x, right_top_x)
print((right_top_x - left_down_x)**2)