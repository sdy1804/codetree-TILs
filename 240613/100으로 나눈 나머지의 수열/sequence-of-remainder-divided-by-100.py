N = int(input())

def like_Fibonacci(N):
    if N == 1:
        return 2
    if N == 2:
        return 4
    return (like_Fibonacci(N-1) * like_Fibonacci(N-2)) % 100

print(like_Fibonacci(N))