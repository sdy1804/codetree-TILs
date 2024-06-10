string = input()
ee_cnt = 0
eb_cnt = 0

for i in range(len(string)-1):
    if string[i] == 'e' and string[i+1] == 'e':
        ee_cnt += 1
    if string[i] == 'e' and string[i+1] == 'b':
        eb_cnt += 1
print(ee_cnt, eb_cnt)