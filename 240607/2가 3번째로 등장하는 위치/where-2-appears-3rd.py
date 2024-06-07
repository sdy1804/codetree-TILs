n = int(input())
arr = list(map(int, input().split()))
index_cnt = 0

for i in range(3):
    if 2 in arr:
        j = arr.index(2)
        arr = arr[j+1:]
        index_cnt += (j+1) 
print(index_cnt)