def grow_down_up(n):
    if n == 0:
        return
    else:
        print("* " * n)
        grow_down_up(n-1)
        print("* " * n)

N = int(input())
grow_down_up(N)