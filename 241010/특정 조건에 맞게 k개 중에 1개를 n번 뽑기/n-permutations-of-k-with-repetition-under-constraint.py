K, N = map(int, input().split())

ans = []

def ans_print(ans):
    for elem in ans:
        print(elem, end=" ")
    print()

def Choose(curr_num):
    if len(ans) >= 3:
        for idx in range(len(ans)-2):
            if ans[idx] == ans[idx+1] == ans[idx+2]:
                return
    if curr_num == N+1:
        ans_print(ans)
        return
    
    for i in range(1, K+1):
        ans.append(i)
        Choose(curr_num+1)
        ans.pop()

    return

Choose(1)