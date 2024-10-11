n = int(input())

visited = [False] * (n+1)
ans = []

def ans_print():
    for elem in ans:
        print(elem, end=' ')
    print()

def Choose(curr_num):
    if curr_num == n+1:
        ans_print()
        return
    
    for i in range(1, n+1):
        if visited[i]:  # 방문 표시가 있으면 패스
            continue
        
        visited[i] = True  # 넣은 숫자에 대해 방문 표시
        ans.append(i)   # 해당 숫자 삽입

        Choose(curr_num+1) # 다음 자릿수로 넘김 (종료 조건으로 가기 위함)

        ans.pop() # 끝자리까지 갔다가 재귀 종료 시 자리를 비워주기 위함
        visited[i] = False # 숫자 뺐으니 방문표시도 뺌
    
Choose(1)