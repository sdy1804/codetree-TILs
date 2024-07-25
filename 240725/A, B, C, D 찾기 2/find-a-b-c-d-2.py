arr = list(map(int, input().split()))

# sorting을 먼저 해야 할지?
# 아무래도 큰 값들을 더해서 작은 값이 나오는 경우는 없으니 sorting을 해야 할듯
# 소팅 하고 난 이후, 4개씩 뽑아놓고 4개에 대한 2개씩 합, 3개씩 합, 4개의 합에 대한 값들을 리스트에 append
# 임시 리스트가 arr과 똑같은 시점에서 break하고 답을 냄

arr.sort()
# print(arr)
A,B,C,D = 0,0,0,0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            for l in range(k+1, len(arr)):
                if arr[i]+arr[j]+arr[k]+arr[l] == max(arr):
                    A, B, C, D = arr[i], arr[j], arr[k], arr[l]
print(A,B,C,D)