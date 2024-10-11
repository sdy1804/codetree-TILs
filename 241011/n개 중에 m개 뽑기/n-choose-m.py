N, M = map(int, input().split())

# 조합 : 123 끝
# 순열 : 123, 132, 213, 231... 뽑고 나서 순서도 중요
ans = []

def ans_print(ans):
    for elem in ans:
        print(elem, end=" ")
    print()

def Choose(curr_num, cnt):
    if curr_num == N+1:
        if cnt == M:
            ans_print(ans)
        return
    
    ans.append(curr_num)
    # print('curr_num, cnt', curr_num, cnt)
    # print(ans)
    Choose(curr_num+1, cnt+1)
    ans.pop()

    # print('second curr_num, cnt', curr_num, cnt)
    # print(ans)
    Choose(curr_num+1, cnt)
    

Choose(1, 0)