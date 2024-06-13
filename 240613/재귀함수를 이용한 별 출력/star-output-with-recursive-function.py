def right_triangle(n):
    if n == 0:
        return
    else:
        right_triangle(n-1)
        print('*' * n)

N = int(input())
right_triangle(N)