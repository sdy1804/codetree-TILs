n, m = map(int, input().split())
seq = list(map(int, input().split()))

def sum_seq():
    sums = 0
    global m, n
    for i in range(n):
        if m != 1:
            sums += seq[m - 1]
        else:
            sums += seq[m - 1]
            break
        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    return sums

print(sum_seq())