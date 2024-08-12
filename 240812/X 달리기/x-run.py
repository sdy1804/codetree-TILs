X = int(input())

# 속력을 증가시킬지, 유지시킬지, 감소시킬지를 판단
# 1로 마무리하는 문제 조건을 지키면서 속력을 정할 수 있는 방법?
# 매번 속력을 증가시켜도 되는지 확인

curr_speed = 1
left_dist = X
curr_time = 0

while True:
    left_dist -= curr_speed
    curr_time += 1

    if left_dist == 0:
        break
    # 증가시켰을 때 이동거리 -> v+1 + v + v-1 + ... + 2 + 1 = (v+1) * (v+2) / 2
    if left_dist >= (curr_speed + 1) * (curr_speed + 2) / 2:
        curr_speed += 1
    # 유지시켰을 때 이동거리 -> v + v-1 + ... + 2 + 1 = v * (v+1) / 2
    elif left_dist >= (curr_speed + 1) * curr_speed / 2:
        pass
    # 이 외에는 속도 감소
    else:
        curr_speed -= 1
print(curr_time)