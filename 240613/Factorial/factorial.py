N = int(input())

def Factorial(n):
    if n == 1:
        return 1
    return Factorial(n-1) * n

print(Factorial(N))