def sum_ten_divide(n):
    sums = 0
    for i in range(1, n+1):
        sums += i
    return sums // 10

N = int(input())
print(sum_ten_divide(N))