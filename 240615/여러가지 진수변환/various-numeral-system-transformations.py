N, B = map(int, input().split())

def change_num(change, n):
    arr = []
    if change == 4:
        while 1:
            if n < 4:
                arr.append(n % 4)
                break
            arr.append(n % 4)
            n //= 4
    elif change == 8:
        while 1:
            if n < 8:
                arr.append(n % 8)
                break
            arr.append(n % 8)
            n //= 8
    return arr

for elem in change_num(B, N)[::-1]:
    print(elem, end="")