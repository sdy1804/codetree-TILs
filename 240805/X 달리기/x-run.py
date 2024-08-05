X = int(input())

dist = 0
velo = 1
time = 0
while dist < 10:
    time += 1
    dist += 1 * velo
    # print(dist, time)
    if dist < X // 2:
        velo += 1
    else:
        if velo > 1:
            velo -= 1
        elif velo == 1:
            velo = 1
print(time)