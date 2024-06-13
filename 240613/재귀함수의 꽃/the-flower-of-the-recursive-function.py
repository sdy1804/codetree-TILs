def up_and_down(n):
    if n == 0:
        return
    else:
        print(n, end=" ")
        up_and_down(n-1)
        print(n, end=" ")


N = int(input())
up_and_down(N)