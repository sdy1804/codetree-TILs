n = int(input())
cnt = 0

while 1:
    if n >= 1000:
        print(cnt)
        break
    else:
        if n % 2 == 0:
            n = n * 3 + 1
            cnt += 1
        elif n % 2 != 0:
            n = n * 2 + 2
            cnt += 1