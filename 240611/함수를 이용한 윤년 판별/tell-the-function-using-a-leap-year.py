def leap_year(n):
    if n % 4 != 0:
        return False
    if n % 100 == 0 and n % 400 != 0:
        return False
    return True

y = int(input())
if leap_year(y):
    print("true")
else:
    print('false')