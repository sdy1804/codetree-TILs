a, b = map(int, input().split())
sum = 0

if a > b:
    for i in range(b, a+1):
        if i % 5 == 0:
            sum += i
    print(sum)
elif a < b:
    for i in range(a, b+1):
        if i % 5 == 0:
            sum += i
    print(sum)