a, b, c = map(int, input().split())

def count_mins(d, h, m):
    day = 0
    hour, mins, elapsed_time = 0, 0, 0
    while 1:
        if hour == h and mins == m:
            break
        if mins == 60:
            hour += 1
            mins = 0
        mins += 1
        elapsed_time += 1
    elapsed_time += d * 60 * 24
    return elapsed_time

if (count_mins(a, b, c) - count_mins(11, 11, 11)) >= 0:
    print(count_mins(a, b, c) - count_mins(11, 11, 11))
else:
    print(-1)