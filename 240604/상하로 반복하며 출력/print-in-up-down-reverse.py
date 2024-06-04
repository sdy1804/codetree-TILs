n = int(input())
up = 1
down = n

for i in range(1, n+1):
    for j in range(n):
        if j % 2 == 0:
            print(up, end="")
        else:
            print(down, end="")
    if up == n:
        up = 1
    else:
        up += 1
    
    if down == 1:
        down = n
    else:
        down -= 1
    print()