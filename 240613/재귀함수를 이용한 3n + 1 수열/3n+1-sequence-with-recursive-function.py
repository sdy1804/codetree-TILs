n = int(input())
cnt = 0

def seq(n):
    global cnt
    if n == 1:
        return cnt
    if n % 2 == 0:
        cnt += 1
        return seq(n // 2)
    else:
        cnt += 1
        return seq(3*n + 1)

print(seq(n))