n = int(input())
cnt = 0

while 1:
    if n == 1:
        print(cnt)
        break
    if n % 2 == 0:
        n = n // 2
        cnt += 1
    elif n % 2 != 0:
        n = n * 3 + 1
        cnt += 1