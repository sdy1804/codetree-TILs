N = int(input())
array = list(map(int, input().split()))

def max_val(n):
    # print(f"max_val{n} is called")
    arr = array[:n]
    if n == 1:
        return arr[0]

    max_value = max_val(n-1)
    if max_value > arr[n-1]:
        return max_value
    else:
        max_value = arr[n-1]
        return max_value
        

print(max_val(N))