def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return recursive_sum(n-1) + n

N = int(input())
print(recursive_sum(N))