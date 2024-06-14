n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    great_value = 0
    if a > b:
        for i in range(1, b+1):
            if a % i == 0 and b % i == 0:
                great_value = i
    else:
        for i in range(1, a+1):
            if a % i == 0 and b % i == 0:
                great_value = i
    return great_value

def lcd(n):
    lower_case = 0
    if n == 1:
        return arr[0]
    lower_case = int((lcd(n-1) * arr[n-1]) / gcd(lcd(n-1), arr[n-1]))
    return lower_case

print(lcd(n))