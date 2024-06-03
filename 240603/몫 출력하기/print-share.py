cnt = 0
while 1:
    # print("cnt", cnt)
    if cnt < 3:
        n = int(input())
    else:
        break
    if n % 2 == 0:
        if cnt <= 3:
            quot = n // 2
            print(quot)
            cnt += 1
        else:
            break
    else:
        continue