a, b = map(int, input().split())
satisfied = False

for i in range(a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        satisfied = True
        break
if satisfied == True:
    print(1)
else:
    print(0)