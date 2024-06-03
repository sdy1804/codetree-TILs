n = int(input())
div = 0
cnt = 0

for i in range(1, n+1):
    div = n // i
    cnt += 1
    if div <= 1:
        print(cnt)
        break
    n = div