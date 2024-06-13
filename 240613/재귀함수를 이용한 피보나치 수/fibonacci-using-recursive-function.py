N = int(input())

def Fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return Fibonacci(n-2) + Fibonacci(n-1)

print(Fibonacci(N))