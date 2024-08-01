x1, x2, x3, x4 = map(int, input().split())

if (x2 > x3) or (x4 > x1) or (x1 < x3 and x4 < x2) or (x3 < x1 and x2 < x4):
    print('intersecting')
else:
    print('nonintersecting')