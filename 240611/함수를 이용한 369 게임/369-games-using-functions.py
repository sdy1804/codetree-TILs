def is_three(n):
    return n % 3 == 0

def is_three_six_nine(n):
    return n % 10 == 3 or n % 10 == 6 or n % 10 == 9 or n // 10 == 3 or n // 10 == 6 or n // 10 == 9 or is_three(n) 


A, B = map(int, input().split())
cnt = 0
for i in range(A, B+1):
    if is_three_six_nine(i) == True:
        cnt += 1
print(cnt)