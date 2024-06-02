three_cnt, five_cnt = 0, 0

for i in range(10):
    num = int(input())
    if num % 3 == 0:
        three_cnt += 1
    if num % 5 == 0:
        five_cnt += 1
print(three_cnt, five_cnt)