N = int(input())
array = list(map(int, input().split()))

def max_val(n, arr):
    max_value = 0
    if n == 1:
        return arr[n-1]
    if max_val(n-1, arr[:n-1]) < arr[n-1]:
        max_value = arr[n-1]
        return max_value
    else:
        max_value = max_val(n-1, arr[:n-1])
        return max_value
        

print(max_val(N, array))