K, N = map(int, input().split())

ans = []

def ans_print(ans):
    for elem in ans:
        print(elem, end=" ")
    print()

def Choose(curr_num):
    if curr_num == N+1:
        ans_print(ans)
        return
    
    for i in range(1, K+1):
        ans.append(i)
        Choose(curr_num+1)
        ans.pop()
    return

Choose(1)