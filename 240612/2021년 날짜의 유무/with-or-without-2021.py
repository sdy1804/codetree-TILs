def is_days(m, d):
    if m >= 1 and m <= 12:
        if m == 2 and d >= 1 and d <= 28:
            return True
        else:
            return False
        if m < 8 and m % 2 != 0:
            if d >= 1 and d <= 31:
                return True
        elif m < 8 and m % 2 == 0:
            if d >= 1 and d <= 30:
                return True
        elif m >= 8 and m % 2 != 0:
            if d >= 1 and d <= 30:
                return True
        elif m >= 8 and m % 2 == 0:
            if d >= 1 and d <= 31:
                return True
    else:
        return False


M, D = map(int, input().split())
if is_days(M, D):
    print("Yes")
else:
    print('No')