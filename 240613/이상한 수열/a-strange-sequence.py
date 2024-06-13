N = int(input())

def weird_seq(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    return weird_seq(N//3) + weird_seq(N-1)


print(weird_seq(N))