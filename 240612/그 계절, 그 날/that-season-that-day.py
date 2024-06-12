def leaf_year(n):
    if n % 4 == 0 and n % 100 == 0 and n % 400 == 0:
        return True
    if n % 4 == 0 and n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False

def check_days(y, m, d):
    if leaf_year(y):
        if m == 2:
            if d >= 1 and d <= 29:
                return True
            else:
                return False
        if m < 8 and m % 2 != 0:
            if d >= 1 and d <= 31:
                return True
            else:
                return False
        if m < 8 and m % 2 == 0:
            if d >= 1 and d <= 30:
                return True
            else:
                return False
        if m >= 8 and m % 2 != 0:
            if d >= 1 and d <= 30:
                return True
            else:
                return False
        if m < 8 and m % 2 == 0:
            if d >= 1 and d <= 31:
                return True
            else:
                return False
    elif leaf_year(y) == False:
        if m == 2:
            if d >= 1 and d <= 28:
                return True
            else:
                return False
        if m < 8 and m % 2 != 0:
            if d >= 1 and d <= 31:
                return True
            else:
                return False
        if m < 8 and m % 2 == 0:
            if d >= 1 and d <= 30:
                return True
            else:
                return False
        if m >= 8 and m % 2 != 0:
            if d >= 1 and d <= 30:
                return True
            else:
                return False
        if m <= 8 and m % 2 == 0:
            if d >= 1 and d <= 31:
                return True
            else:
                return False

def check_season(y, m, d):
    if check_days(y, m, d):
        if m >= 3 and m <= 5:
            print('Spring')
        elif m >= 6 and m <= 8:
            print('Summer')
        elif m >= 9 and m <= 11:
            print('Fall')
        else:
            print('Winter')
    else:
        print(-1)

Y, M, D = map(int, input().split())
check_season(Y, M, D)