n = int(input())
To_right_start = 1

for i in range(n):
    if i == 0:
        for j in range(n):
            print(To_right_start, end=" ")
            if To_right_start == n:
                continue
            else:     
                To_right_start += 1
        print()
    elif i % 2 != 0:
        To_right_start += n
        for j in range(n):
            print(To_right_start, end=" ")
            if j == (n-1):
                continue
            else:
                To_right_start -= 1
        print()
    else:
        To_right_start += n
        for j in range(n):
            print(To_right_start, end=" ")
            if j == (n-1):
                continue
            else:
                To_right_start += 1
        print()