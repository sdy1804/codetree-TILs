x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

if x2 < a1 or a2 < x1 or y1 > b2 or b1 > y2:
    print('nonoverlapping')
else:
    print('overlapping')