x1, x2, x3, x4 = map(int, input().split())

if (x1< x3 and x3 < x2 and x2 < x4) or (x3 < x1 and x1 < x4 and x4 < x2) or (x1 < x3 and x4 < x2) or (x3 < x1 and x2 < x4):
    print('intersecting')
else:
    print('nonintersecting')