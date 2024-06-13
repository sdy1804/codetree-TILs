def print_Hello(n):
    if n == 0:
        return
    else:
        print_Hello(n-1)
        print('HelloWorld')

N = int(input())
print_Hello(N)