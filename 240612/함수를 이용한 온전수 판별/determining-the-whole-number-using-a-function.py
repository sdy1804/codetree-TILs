def perfect_num(A, B):
    cnt = 0
    for i in range(A, B+1):
        if i % 2 == 0:
            continue
        elif i % 10 == 5:
            continue
        elif i % 3 == 0 and i % 9 != 0:
            continue
        else:
            cnt += 1
    return cnt

a, b = map(int, input().split())
print(perfect_num(a, b))