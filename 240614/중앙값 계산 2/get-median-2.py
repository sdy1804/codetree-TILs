n = int(input())
arr = list(map(int, input().split()))

def mid_val(array):
    if len(array) == 1:
        return array[0]
    array.sort()
    return array[(0 + len(array)) // 2]
    

for i in range(len(arr)):
    if i % 2 == 0:
        new_arr = arr[:i+1]
        print(mid_val(new_arr), end=" ")