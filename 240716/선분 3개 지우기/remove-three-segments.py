n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 3개 선분을 고른다
# 3개 선분을 제외한다 -> arr을 복사한 리스트에서 해당될 경우 삭제
# 나머지 선분들끼리 겹치는지 확인한다 -> 완전탐색으로 x,y 값 비교해서 겹치는지 확인
# 겹치치 않으면 cnt+=1 한다

cnt = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            # print(arr[i], arr[j], arr[k])
            arr_copy = arr.copy()
            if arr[i] in arr_copy and arr[j] in arr_copy and arr[k] in arr_copy: # 임시 리스트에서 고른 3개 선분 제외
                arr_copy.remove(arr[i])
                arr_copy.remove(arr[j])
                arr_copy.remove(arr[k])
            # print(arr_copy)
            fold = False
            for l in range(len(arr_copy)):
                for m in range(l+1, len(arr_copy)):
                    # print(arr_copy[l], arr_copy[m])
                    if arr_copy[l][0] <= arr_copy[m][0] and arr_copy[l][1] >= arr_copy[m][0] and arr_copy[l][1] <= arr_copy[m][1]: # 겹칠 수 있는 여러가지 경우의 수 생각해야 함
                        fold = True
                    if arr_copy[l][0] >= arr_copy[m][0] and arr_copy[l][1] <= arr_copy[m][1]:
                        fold = True
                    if arr_copy[m][0] <= arr_copy[l][0] and arr_copy[m][1] >= arr_copy[l][0] and arr_copy[m][1] <= arr_copy[l][1]:
                        fold = True
                    if arr_copy[m][0] >= arr_copy[l][0] and arr_copy[m][1] <= arr_copy[l][1]:
                        fold = True
                    if arr_copy[l][1] == arr_copy[m][0] or arr_copy[m][1] == arr_copy[l][0]:
                        fold = True
            if fold:
                cnt += 0
            else:
                cnt += 1
print(cnt)