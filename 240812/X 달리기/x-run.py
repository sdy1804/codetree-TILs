X = int(input())

# 언제 증가, 언제 감소, 언제 유지할지?
# 현재 속도를 올리거나 유지했을 때 문제 조건을 만족하면서 도달 가능한지 체크
# 이에 따라 증가, 유지, 감소 선택 가능

dist = 0
velo = 1
time = 0
while dist < X:
    time += 1
    dist += 1 * velo
    # print('dist, time, velo', dist, time, velo)
    if dist < X // 2:
        velo += 1
    elif dist == X // 2:
        velo = velo
    else:
        if velo > 1:
            velo -= 1
        elif velo == 1:
            velo = 1
print(time)

# 6
# dist, time, velo 1 1 1 -> 속도 증가 시(2), X-dist=3 > 현재속도(2) 이므로 가능.
# dist, time, velo 3 2 2 -> 속도 증가 시(3), X-dist=0 < 현재속도(3)이므로 불가 / 속도 유지시(2), X-dist=1이며 (현재속도-1)이 1이므로 가능
# dist, time, velo 5 3 2 -> X - dist가 1이므로 현재속도(2)에서 감소
# dist, time, velo 6 4 1

# 7
# dist, time, velo 1 1 1 -> 속도 증가 시(2), X-dist=4 > 현재속도(2) 이므로 가능.
# dist, time, velo 3 2 2 -> 속도 증가 시(3), X-dist=1 < 현재속도(3) 이므로 불가능. / 속도 유지 시(2), X-dist=2
# dist, time, velo 5 3 2 -> 속도 증가시(3), 총 dist가 X보다 커짐 / 속도 유지시(2), 총 dist = X됨 / 속도 감소 시, 속도와 남은 거리 차가 0이므로 가능
# dist, time, velo 6 4 1
# dist, time, velo 7 5 1

# 8
# dist, time, velo 1 1 1 -> 속도 증가시, dist(5) > 속도(2) 이므로 가능.
# dist, time, velo 3 2 2 -> 속도 증가시, dist(3) = 속도(3) 이므로 
# dist, time, velo 5 3 2
# dist, time, velo 7 4 2
# dist, time, velo 8 5 1

# 9 
# dist, time, velo 1 1 1
# dist, time, velo 3 2 2
# dist, time, velo 6 3 3
# dist, time, velo 8 4 2
# dist, time, velo 9 5 1

# 10
# dist, time, velo 1 1 1
# dist, time, velo 3 2 2
# dist, time, velo 6 3 3
# dist, time, velo 8 4 2
# dist, time, velo 9 5 1
# dist, time, velo 10 6 1

# 11
# dist, time, velo 1 1 1
# dist, time, velo 3 2 2
# dist, time, velo 6 3 3
# dist, time, velo 8 4 2
# dist, time, velo 10 5 2
# dist, time, velo 11 6 1