N, C, G, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def get_temp(Ta, Tb, temp):
    if temp < Ta:
        return C
    if temp >= Ta and temp <= Tb:
        return G
    if temp > Tb:
        return H

total_max = 0
for i in range(1000):
    work_output = 0
    for j in range(len(arr)):
        work_output += get_temp(arr[j][0], arr[j][1], i)
    total_max = max(total_max, work_output)
print(total_max)