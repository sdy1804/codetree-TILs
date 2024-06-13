def positional_squ(n):
    if n < 10:
        return n**2
    else:
        return positional_squ(n // 10) + (n % 10)**2


N = int(input())
print(positional_squ(N))