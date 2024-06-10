string = input()
sum = 0

for s in string:
    if s.isdigit() == True:
        s = int(s)
        sum += s
print(sum)