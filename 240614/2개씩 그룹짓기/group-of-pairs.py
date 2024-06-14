n = int(input())
arr = list(map(int, input().split()))

arr.sort()

def max_val():
    max_value = arr[0] + arr[-1]
    for i in range(n): # 0   1   2
        if max_value < arr[i] + arr[-(i+1)]: # 1 + -2, 2 + -3, 3+ -4
            max_value = arr[i] + arr[-(i+1)]
    return max_value

print(max_val())