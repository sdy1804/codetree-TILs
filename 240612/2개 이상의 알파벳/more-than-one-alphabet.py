def check_alpha(string):
    cnt = 0
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            cnt += 1
    return cnt

A = input()
if check_alpha(A) >= 1:
    print('Yes')
else:
    print('No')