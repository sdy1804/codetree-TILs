n = int(input())
cnt = n

for i in range(n):
    for j in range(i+1):
        if j == 0:
            cnt = n
        if i == 0:
            print(cnt, end=" ")
        elif i >= 1:
            print(cnt-i, end=" ")
            cnt += 1
    print()