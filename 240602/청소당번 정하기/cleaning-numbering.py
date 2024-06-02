n = int(input())

class_cnt, hall_cnt, toilet_cnt = 0, 0, 0

for i in range(1, n+1):
    # print(i)
    if i % 12 == 0:
        toilet_cnt += 1
    elif i % 6 == 0 or i % 3 == 0:
        hall_cnt += 1
    elif i % 2 == 0:
        class_cnt += 1

print(class_cnt, hall_cnt, toilet_cnt)