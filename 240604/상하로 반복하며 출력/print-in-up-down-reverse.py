n = int(input())
up = 1
down = n

for i in range(1, n+1):
    for j in range(n):
        if j % 2 == 0:
            print(up, end="")
        else:
            print(down, end="")
    if up == 4:
        up = 1
    else:
        up += 1
    
    if down == 1:
        down = 4
    else:
        down -= 1
    print()