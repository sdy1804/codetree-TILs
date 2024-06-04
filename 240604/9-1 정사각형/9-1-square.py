n = int(input())
cnt = 9

for _ in range(n):
    for _ in range(n):
        print(cnt, end="")
        if cnt == 1:
            cnt = 9
        else:
            cnt -= 1
    print()