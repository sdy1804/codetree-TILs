m = int(input())

for i in range(m):
    n = int(input())
    cnt = 0

    while 1:
        if n == 1:
            break
        if n % 2 == 0:
            n //= 2
            cnt += 1
        else:
            n = 3*n + 1
            cnt += 1
    print(cnt)