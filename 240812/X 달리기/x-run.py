X = int(input())

curr_pos = 0
curr_speed = 1
sum_time = 0
while (True):
    curr_pos += curr_speed
    sum_time += 1
    curr_speed += 1
    increase_sum = 0

    if (curr_pos == X):
        break
    
    for i in range(curr_speed):
        increase_sum += i
    if X - (curr_pos + curr_speed) < increase_sum:
        curr_speed -= 1
    
    stay_sum = 0
    for i in range(curr_speed):
        stay_sum += i
    if X - (curr_pos + curr_speed) < stay_sum:
        curr_speed -= 1

print(sum_time)