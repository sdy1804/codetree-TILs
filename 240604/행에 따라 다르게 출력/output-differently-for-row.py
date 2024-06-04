n = int(input())
odd_start = 1

for i in range(n):
    if i == 0:
        for j in range(n):
            print(odd_start, end=" ")
            if j == (n-1):
                continue
            else:
                odd_start += 1
        print()
    elif i % 2 != 0:
        odd_start += 2
        for j in range(n):
            print(odd_start, end=" ")
            if j == (n-1):
                continue
            else:
                odd_start += 2
        print()
    else:
        odd_start += 1
        for j in range(n):
            print(odd_start, end=" ")
            if j == (n-1):
                continue
            else:
                odd_start += 1
        print()