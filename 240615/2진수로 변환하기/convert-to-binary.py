n = int(input())

def binary(N):
    arr = []
    while 1:
        if N < 2:
            arr.append(N)
            break
        arr.append(N % 2)
        N //= 2
    return arr

for elem in binary(n)[::-1]:
    print(elem, end="")