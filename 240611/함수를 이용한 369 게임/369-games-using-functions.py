def is_three(n):
    return n % 3 == 0

def is_three_six_nine(n):
    n = str(n)
    return '3' in n or '6' in n or '9' in n or is_three(int(n)) 


A, B = map(int, input().split())
cnt = 0
for i in range(A, B+1):
    if is_three_six_nine(i) == True:
        cnt += 1
print(cnt)