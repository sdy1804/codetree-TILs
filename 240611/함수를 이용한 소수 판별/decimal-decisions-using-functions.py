def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


A, B = map(int, input().split())
sums = 0
for i in range(A, B+1):
    if is_prime(i):
        sums += i
print(sums)