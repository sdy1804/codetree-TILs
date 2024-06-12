def is_even(n):
    if n < 10:
        if n % 2 == 0:
            return True
    else:
        n = str(n)
        if (int(n[0]) + int(n[1])) % 2 == 0:
            return True

def is_prime(n):
    for j in range(2, i):
        if n % j == 0:
            return False
    return True


a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if is_even(i) and is_prime(i):
        cnt += 1
print(cnt)