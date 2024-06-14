class Point:
    def __init__(self, x, y, num=0):
        self.x = x
        self.y = y
        self.num = num

def distance(x, y):
    return abs(x) + abs(y)

N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append(Point(x, y))

for idx, std in enumerate(arr, start=1):
    std.num = idx

arr.sort(lambda x: distance(x.x, x.y))

for std in arr:
    print(std.num)