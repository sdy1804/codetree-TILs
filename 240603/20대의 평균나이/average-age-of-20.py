num = 0
sum, avg = 0 , 0

while 1:
    n = int(input())
    if n < 20 or n > 29:
        print(f"{avg:.2f}")
        break
    else:
        sum += n
        num += 1
        avg = sum / num