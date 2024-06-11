def minimum(*arg):
    mins_ = min(arg)
    return mins_

a, b, c = map(int, input().split())
print(minimum(a, b, c))