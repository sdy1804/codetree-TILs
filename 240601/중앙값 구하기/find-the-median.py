a, b, c = map(int, input().split())

if a > b: # a 20, b 10
    if a < c and b < c: # a 20 b 10 c 30
        print(a)
    elif a > c and b < c: # a 20 b 10 c 15
        print(c)
    elif a > c and b > c: # a 20 b 10 c 5
        print(b)
elif a < b: # a 10, b 20
    if a < c and b < c: # a 10, b 20, c 30
        print(b)
    elif a < c and c < b: # a 10, b 20, c 15
        print(c)
    elif a > c and b > c: # a 10, b 20, c 5
        print(a)