a, b, c = map(int, input().split())

if a <= b and a < c:
    print(a)
elif a < b and a <= c:
    print(a)

elif b <= a and b < c:
    print(b)
elif b < a and b <= c:
    print(b)


elif c <= a and c < b:
    print(c)
elif c < a and c <= b:
    print(c)