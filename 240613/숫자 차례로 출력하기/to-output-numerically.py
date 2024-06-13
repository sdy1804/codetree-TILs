def ascending(n):
    if n == 0:
        return
    else:
        ascending(n-1)
        print(n, end=" ")

def descending(n):
    if n == 0:
        return
    else:
        print(n, end=" ")
        descending(n-1)

N = int(input())
ascending(N)
print()
descending(N)