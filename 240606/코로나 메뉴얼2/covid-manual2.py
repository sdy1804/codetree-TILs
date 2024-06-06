clinic = [0]*4
for i in range(3):
    sym, temp = input().split()
    temp = int(temp)
    if sym == 'Y' and temp >= 37:
        clinic[0] += 1
    elif sym == 'N' and temp >= 37:
        clinic[1] += 1
    elif sym == 'Y' and temp < 37:
        clinic[2] += 1
    else:
        clinic[3] += 1

for i in range(len(clinic)):
    print(clinic[i], end=' ')
if clinic[0] >= 2:
    print('E')