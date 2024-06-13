N = int(input())

def even_or_odd(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return even_or_odd(n-2) + n

print(even_or_odd(N))